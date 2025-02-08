from flask import Flask, render_template

app = Flask(__name__,static_folder='static',template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/return')
def return_page():
    data = "hello"
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)