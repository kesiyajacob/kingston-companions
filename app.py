from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Activity
from werkzeug.security import generate_password_hash, check_password_hash
import openai
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
        return redirect(url_for("match"))

    return render_template("index.html")


#------Match route----------------------------------


@app.route("/match")
def match():
    username = session.get("username")
    if not username:
        return redirect(url_for("index"))
    
    user = User.query.filter_by(username=username).first()
    other_users = User.query.filter(User.username != username).all()
    activities = Activity.query.all()
    
    if not other_users:
        return "No other users to match with yet."
    
    # Use mock response during development
    if USE_MOCK_RESPONSE:
        match_data = {
            'greeting': "Hey Bobert! I've found someone you might enjoy meeting!",
            'match_name': "Carol",
            'match_reason': "You both have that creative spark - you with your baking and archery, and Carol with her painting and cooking. I can already imagine you two swapping recipes and sharing stories!",
            'activities': [
                {
                    'name': 'Crock A Doodle',
                    'description': "Perfect for Carol's artistic side, and you'd enjoy the creative outlet too. Chat while you paint!"
                },
                {
                    'name': 'Strategies Board Game Café',
                    'description': "Carol loves board games! Grab coffee and enjoy some friendly competition."
                },
                {
                    'name': 'Victoria Park',
                    'description': "Take a leisurely walk and just talk. The best friendships grow in simple moments."
                }
            ],
            'closing': "I have a really good feeling about you two! 😊"
        }
        return render_template("match.html", username=username, match=match_data)

    
    # Build prompt - speaking TO the user
    prompt = f"""
I'm helping {user.username} find a friend to connect with.

{user.username}'s interests: {user.interests}
{user.username}'s bio: {user.bio}

Here are some potential friends:
"""
    for u in other_users:
        prompt += f"- {u.username}: Interests in {u.interests}. {u.bio}\n"
    
    prompt += "\nActivities they could do together:\n"
    for act in activities:
        prompt += f"- {act.name}: {act.description} (Keywords: {act.keywords})\n"
    
    prompt += f"\nPlease talk directly to {user.username}. Suggest who would be a great friend match and recommend 1-3 activities they'd enjoy together. Be warm, conversational, and natural - like a friendly matchmaker, not a formal report."
    
    # Call OpenAI Chat Completions API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a warm, friendly matchmaker helping seniors find friendship. Speak directly to the user in a natural, conversational way. Avoid repetition and be concise but personable."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=500
    )
    
    result_text = response.choices[0].message.content.strip()
    return render_template("match.html", username=username, result=result_text)



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


