from flask import Flask, render_template, jsonify,request

app = Flask(__name__,static_folder='static',template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/addtolist')
def addtolist():
    return 200

@app.route('/return',methods=["POST"])
def return_page():
    data = {"recvd": request.json['message']}
    return jsonify(data)

@app.route('/news')
def news():
    return "Youre average so far is......"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)