from flask import Flask, render_template, jsonify,request, session, redirect, url_for, flash
import functools

def login_required(view):
    """Decorator to ensure a user is logged in before accessing a view."""
    @functools.wraps(view)  # Preserve original function metadata
    def wrapped_view(*args, **kwargs):
        if not session.get('user_id'):  # Check if user is logged in
            flash("You must be logged in to view this page.", "danger")  # Optional flash message
            return redirect(url_for('signin'))  # Redirect to login page
        return view(*args, **kwargs)  # User is logged in, proceed to the view
    return wrapped_view

app = Flask(__name__,static_folder='static',template_folder='templates')
#change secret key before deployment
app.secret_key = "goose"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin')
def signin():
    return render_template('signin.html') 

@app.route('/addtolist')
@login_required
def addtolist():
    return 200

@app.route('/return',methods=["POST"])
@login_required
def return_page():
    data = {"recvd": request.json['message']}
    return jsonify(data)

@app.route('/news')
def news():
    #add rate limiter of something so it doesnt get called too much
    return "Youre average so far is......"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)