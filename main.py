from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    guessData = db.GetAllGuesses() 
    return render_template("index.html", guesses=guessData) 

@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        
        user = db.CheckLogin(username, password)
        if user:
            
            session['id'] = user['id']
            session['username'] = user['username']

           
            return redirect("/")


    
    return render_template("login.html")

@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")
@app.route("/register", methods=["GET", "POST"])
def Register():

    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

       
        if db.RegisterUser(username, password):
            
            return redirect("/")
       
    return render_template("register.html")

@app.route("/add", methods=["GET","POST"])
def Add():
    if session.get('username') == None:
        return redirect("/")
    
    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        game = request.form['game']
        score = request.form['score']
        review = request.form['review']

       
        db.AddGuess(user_id, date, game, score, review)

    return render_template("add.html")



app.run(debug=True, port=5000)