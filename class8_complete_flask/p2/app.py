from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>\
        <p>Pakistan zinda bad</p>\
        <p>We love our country! <a href='/about'>About</a></p>\
    "

@app.route("/about_student")
def about():
    return '''
    <h1>About NED PGD Class</h1>
    <h2>Machine Learning</h2>
    <hr>
    <p>Hello NED Students!</p>
    '''

app.run(debug=True)