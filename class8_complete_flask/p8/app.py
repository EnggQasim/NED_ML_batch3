from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'] )
def login():
    if request.method == 'GET':
        return f"""
        Method GET
        <h1>Hello Dear, {request.args.get('uname')}</h1>
        <h2>Successfully Signup with {request.args.get('email')}</h2>
        """
    else:
        return f"""
        Method POST
        <h1>Hello Dear, {request.form['uname']}</h1>
        <h2>Successfully Signup with {request.form['email']}</h2>
        """


app.run(debug=True)    
