from flask import Blueprint, render_template, redirect, url_for,Flask,request, session
from database import session as db
from model import User
from sqlalchemy.future import select
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)


registration = {}
SPORTS=["Fotball", "socer","Basket"]



@app.route("/")
def home():
    if not session.get("name"):
        return  redirect("/login")
    return  render_template("index.html", sports=SPORTS)

@app.route("/books")
def books():
    books=None
    return  render_template("books.html", books=books)

@app.route("/cart", methods=["GET","POST"])
def cart():
    if "cart" not in session:
        session["cart"] =[]
    
    if request.method == "POST":
        id=request.form.get("id")
        if id:
            session["cart"].append(id)
        return  redirect("/cart")
    
    books= None
    return  render_template("cart.html", books=books)





@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["name"]=request.form.get("name")
        return  redirect("/")
    return  render_template("login.html")

@app.route("/logout")
def logout():
    session["name"]=None
    return  redirect("/")


@app.route("/register", methods=["POST"])
def register():
    name=request.form.get("name")
    if not name:
        return  render_template("fail.html")
    sport=request.form.get("sport")
    if sport not in SPORTS:
        return  render_template("fail.html")
    registration[name]=sport
    user=User(Name=name,Sport=sport)
    print(user.Name)
    db.add(user)
    db.commit()
    return  render_template("greet.html")

@app.route("/registrans")
def registrans():
    all_user=db.query(User).all()
    return  render_template("registrans.html", registrans=all_user)

@app.route("/deregistr", methods=["POST"] )
def deregistr():
    id=request.form.get("id")
    if id:
        user_to_delete = db.query(User).filter_by(id=id).first()
        db.delete(user_to_delete)
        db.commit()

    return  redirect("/registrans")

app.run(debug=True)
