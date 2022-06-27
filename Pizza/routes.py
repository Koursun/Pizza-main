from Pizza import app, db
from Pizza.models import pizza, customer
from flask import Flask, render_template, request, flash

@app.route('/', methods=["GET","Post"])
def home():

    return render_template("home.html")

@app.route('/user', methods=["GET","Post"])
def user():  #this should work as both a login and register
    if request.method == "POST":
        user = request.form.get('username')
        print(user)
        on = False #when the user is tagging the name, we make the user inactive.
        name = customer.query.filter_by(name=user).first()
        if name:
            print (name.active)
            if name.active == True:
                flash ("use a diffrent username, this one is being used")
                print("sssss")
                return render_template("home.html")
            else:
                flash ("username confirmed, coining name. logged in correctly, ")
                return render_template("fail.html")



        new_customer = customer()
        new_customer.name = user
        new_customer.active = on

        db.session.add(new_customer)
        print (new_customer)
        db.session.commit()

        results = customer.query.all()
        print(results)
        return render_template("logged.html", results = results)






@app.route('/add', methods=["GET","Post"])
def add():
    if request.method == "POST":
        
        
        return render_template("fail.html")

@app.route('/fail')
def fail():
    return render_template("fail.html")



