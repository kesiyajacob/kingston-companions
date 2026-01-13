from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Activity
from werkzeug.security import generate_password_hash, check_password_hash
import openai
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# configure your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friendship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set this to True while styling, False when you want real API calls
USE_MOCK_RESPONSE = True

# connect db to app
db.init_app(app)

with app.app_context():
    db.create_all()

#------Home route----------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        interests = request.form["interests"]
        bio = request.form["bio"]

        user = User.query.filter_by(username=username).first()
        if user:
            user.interests = interests
            user.bio = bio
        else:
            user = User(username=username, interests=interests, bio=bio)
            db.session.add(user)
        db.session.commit()

        session["username"] = username
        return redirect(url_for("dashboard"))

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if not username:
        return redirect(url_for("index"))

    user = User.query.filter_by(username=username).first()
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
            suggestions=activities[:4]
        )

    # ---------- REAL OPENAI MODE ----------
    matched_user = other_users[0]
    suggested_outing = activities[0]

    prompt = f"""
You are a warm, friendly matchmaker helping seniors in Kingston form friendships.

User:
Name: {user.username}
Interests: {user.interests}
Bio: {user.bio}

Potential friend:
Name: {matched_user.username}
Interests: {matched_user.interests}
Bio: {matched_user.bio}

Suggested activity:
Name: {suggested_outing.name}
Description: {suggested_outing.description}

Please respond in this exact format:

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
        suggestions=activities[:4]
    )



#--------------LOGIN------------------------------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth.html', active_tab='login')

#--------------REGISTER-------------------------------------

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method =="POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username not available', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('There is already an account with this email', 'danger')
        else: 
            password_hash= generate_password_hash(password)

            new_user = User(username= username, email=email, password=password_hash)

            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('dashboard'))
    return render_template('auth.html', active_tab='register')


if __name__ == "__main__":
    app.run(debug=True)


