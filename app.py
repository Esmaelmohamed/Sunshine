from flask import Flask , request , render_template ,redirect
from weather import main as get_weather 
from flask_login import login_required
import sqlite3 


app = Flask("__name__") 

dbfile = "/home/esmael/Desktop/weatherapp/weatherapp.db"
con = sqlite3.connect(dbfile) 

cur = con.cursor("SELECT * FROM users") 
print(cur)


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username") 
        password = request.form.get("passwrod")
    return render_template("login.html")


@app.route("/register",methods = ["GET","POST"])
def register():
    return  render_template("register.html")



@app.route("/edit", methods = ["GET","POST"]) 
def edit():
    data = None 
    if request.method == "POST":
       city = request.form['cityName']
       state = request.form['stateName'] 
       country = request.form["countryName"]
       data = get_weather(city,state,country)
       
    return render_template("edit.html",data = data)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        pass
        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 


