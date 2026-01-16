from pydoc import text
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Activity
from werkzeug.security import generate_password_hash, check_password_hash
import openai
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
load_dotenv()

UPLOAD_FOLDER = 'static/profile_pics' 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "supersecretkey"

# configure your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friendship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# Set this to True while styling, False when you want real API calls
USE_MOCK_RESPONSE = False

# connect db to app
db.init_app(app)

with app.app_context():
    db.create_all()


#------Home route----------------------------------

@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))
    

    user = User.query.filter_by(username=username).first()
    if user is None:
        session.pop("username", None)
        return redirect(url_for("login"))


    other_users = User.query.filter(User.username != username).all()
    activities = Activity.query.all()

    if not other_users:
        return "No other users to match with yet."

    # ---------- MOCK MODE ----------
    if USE_MOCK_RESPONSE:
        matched_user = User.query.filter_by(username="Carol").first()
        suggested_outing = Activity.query.filter_by(name="Breakwater Park").first()

        match_reason = (
            "You both enjoy relaxed, creative activities and value good conversation. "
            "Your shared love for calm, social hobbies makes this a natural connection."
        )

        outing_reason = (
            "Breakwater Park offers a peaceful setting for walking and chatting, "
            "which fits both of your interests and energy levels."
        )

        return render_template(
            "dashboard.html",
            user=user,
            match=matched_user,
            outing=suggested_outing,
            match_reason=match_reason,
            outing_reason=outing_reason,
            suggestions = activities[:4]
        )

    # ---------- REAL OPENAI MODE ----------
    import random

# ----- AI: Pick activities user might like -----
    activity_list = ""
    for act in activities:
        activity_list += f"- {act.name}: {act.description}\n"

    activity_prompt = f"""
    User interests: {user.interests}

    Here are available places seniors in Kingston can visit:
    {activity_list}

    Choose the 5 places that best match the user's interests.
    Respond ONLY with a comma-separated list of activity names.
    """

    activity_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You recommend enjoyable outings for seniors."},
            {"role": "user", "content": activity_prompt}
        ],
        temperature=0.7,  # Increased from 0.4 for more variety
        max_tokens=100
    )

    chosen_names = activity_response.choices[0].message.content
    chosen_names = [name.strip() for name in chosen_names.split(",")]
    suggestions = Activity.query.filter(Activity.name.in_(chosen_names)).all()

    # Pick a random activity from suggestions for this match
    suggested_outing = random.choice(suggestions) if suggestions else activities[0]

    # Remove the suggested outing and keep 4 suggestions
    suggestions = [
        activity for activity in suggestions
        if activity.id != suggested_outing.id
    ][:4]


# ----- AI: Find best matching user -----
    users_list = ""
    for other in other_users:
        users_list += f"- {other.username}: Interests: {other.interests}, Bio: {other.bio}\n"

    match_prompt = f"""
    Current user:
    Name: {user.username}
    Interests: {user.interests}
    Bio: {user.bio}

    Potential friends:
    {users_list}

    Who would be the best friend match for {user.username}? Consider shared interests and compatible personalities.
    Respond ONLY with the username of the best match.
    """

    match_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a thoughtful matchmaker helping seniors form meaningful friendships."},
            {"role": "user", "content": match_prompt}
        ],
        temperature=0.7,
        max_tokens=50
    )

    matched_username = match_response.choices[0].message.content.strip()
    matched_user = User.query.filter_by(username=matched_username).first()

# Fallback if AI returns invalid username
    if not matched_user:
        matched_user = random.choice(other_users)

# ----- Generate explanation -----
    prompt = f"""
    You are a warm, friendly matchmaker helping seniors in Kingston form friendships.

    You are speaking directly to:
    User:
    Name: {user.username}
    Interests: {user.interests}
    Bio: {user.bio}

    You're introducing them to a potential friend:
    Name: {matched_user.username}
    Interests: {matched_user.interests}
    Bio: {matched_user.bio}

    Suggested activity:
    Name: {suggested_outing.name}
    Description: {suggested_outing.description}

    Please respond in this exact format, speaking directly to {user.username}:

    MATCH_REASON:
    (2-3 friendly sentences explaining why these two people would get along)

    OUTING_REASON:
    (1-2 sentences explaining why this activity suits both people)
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are kind, conversational, and supportive. Write clearly and warmly for seniors."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=250
    )

    text = response.choices[0].message.content

# --- Simple parsing ---
    match_reason = ""
    outing_reason = ""
    if "MATCH_REASON:" in text and "OUTING_REASON:" in text:
        parts = text.split("OUTING_REASON:")
        match_reason = parts[0].replace("MATCH_REASON:", "").strip()
        outing_reason = parts[1].strip()

    return render_template(
    "dashboard.html",
    user=user,
    match=matched_user,
    outing=suggested_outing,
    match_reason=match_reason,
    outing_reason=outing_reason,
    suggestions=suggestions
)



#--------------LOGIN------------------------------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('dashboard')) 
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth.html', active_tab='login')

#--------------REGISTER-------------------------------------

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        interests = request.form['interests']
        profile_pic = request.files.get('profile_pic')
        mobility_level = request.form['mobility_level']
        
        if User.query.filter_by(username=username).first():
            flash('Username not available', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('There is already an account with this email', 'danger')
        else: 
            password_hash = generate_password_hash(password)
            # Handle profile picture upload
            profile_pic_filename = None
            if profile_pic and profile_pic.filename != '':
                print("DEBUG: Processing profile picture...")
                # Secure the filename
                from werkzeug.utils import secure_filename
                import os
                filename = secure_filename(profile_pic.filename)
                # Create unique filename to avoid conflicts
                import uuid
                unique_filename = f"{uuid.uuid4().hex}_{filename}"
                print(f"DEBUG: unique_filename = {unique_filename}")
                # Define upload folder 
                UPLOAD_FOLDER = 'static/profile_pics'
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                # Save the file
                file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
                print(f"DEBUG: Saving to {file_path}")
                profile_pic.save(file_path)
                profile_pic_filename = unique_filename
                print(f"DEBUG: File saved! profile_pic_filename = {profile_pic_filename}")
            else:
                print("DEBUG: No profile picture or empty filename")
                
            new_user = User(
                username=username, 
                email=email, 
                password=password_hash, 
                bio=bio, 
                interests=interests,
                profile_pic=profile_pic_filename,
                mobility_level=mobility_level
            )
            db.session.add(new_user)
            db.session.commit()
            print(f"DEBUG: User created with profile_pic = {new_user.profile_pic}")
            session['username'] = new_user.username
            return redirect(url_for('dashboard'))
    return render_template('auth.html', active_tab='register')

#--------------LOGOUT-------------------------------------

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login')) 


#--------------VIEW OUTINGS-------------------------------------

@app.route("/outings")
def outings():
    activities = Activity.query.all()
    return render_template("outings.html", activities=activities)




#-----edit profile------------------------------

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username']).first()
    
    if request.method == 'POST':
        # Verify current password
        current_password = request.form['current_password']
        if not check_password_hash(user.password, current_password):
            flash('Incorrect current password', 'danger')
            return render_template('edit_profile.html', user=user)
        
        # Update username and email
        new_username = request.form['username']
        new_email = request.form['email']
        
        # Check if username is taken by another user
        if new_username != user.username:
            if User.query.filter_by(username=new_username).first():
                flash('Username not available', 'danger')
                return render_template('edit_profile.html', user=user)
        
        # Check if email is taken by another user
        if new_email != user.email:
            if User.query.filter_by(email=new_email).first():
                flash('Email already in use', 'danger')
                return render_template('edit_profile.html', user=user)
        
        # Update basic info
        user.username = new_username
        user.email = new_email
        user.bio = request.form['bio']
        user.interests = request.form['interests']
        user.mobility_level = request.form['mobility_level']
        
        # Handle profile picture update
        profile_pic = request.files.get('profile_pic')
        if profile_pic and profile_pic.filename != '':
            from werkzeug.utils import secure_filename
            import os
            import uuid
            
            # Delete old profile pic if exists
            if user.profile_pic:
                old_pic_path = os.path.join('static', 'profile_pics', user.profile_pic)
                if os.path.exists(old_pic_path):
                    os.remove(old_pic_path)
            
            filename = secure_filename(profile_pic.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            
            UPLOAD_FOLDER = os.path.join('static', 'profile_pics')
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            
            file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            profile_pic.save(file_path)
            user.profile_pic = unique_filename
        
        # Update password if provided
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password:
            if new_password != confirm_password:
                flash('New passwords do not match', 'danger')
                return render_template('edit_profile.html', user=user)
            user.password = generate_password_hash(new_password)
        
        db.session.commit()
        session['username'] = user.username  # Update session if username changed
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_profile.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)


