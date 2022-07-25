from Pizza import app, db
from Pizza.models import pizza, customer
from flask import Flask, render_template, request, flash, session, redirect

@app.route('/', methods=["GET","Post"])
def home():

    return render_template("home.html")

@app.route('/user', methods=["GET","Post"])
def user():  #this should work as both a login and register, though, it technically isn't either in my books
    if request.method == "POST":
        user = request.form.get('username')
        print(user)
        on = False #inactive, be sure to change this into True once the website is live
        name = customer.query.filter_by(name=user).first()
        if name:
            print (name.active)
            if name.active == True:
                flash ("use a diffrent username, this one is being used")
                print("sssss")
                return render_template("home.html")
            elif name.active == False:
                flash ("username confirmed, coining name. logged in correctly, ")
                session['username'] = request.form['username']
                customer = request.form['username']
                update_customer = customer()

                update_customer.name = customer
                update_customer.active = False
                db.session.update
                results = customer.query.all()
                print(results)
                return render_template("logged.html", results = results)
            else:
                new_customer = customer()
                new_customer.name = user
                new_customer.active = on

                db.session.add(new_customer)
                print (new_customer)
                db.session.commit()

                results = customer.query.all()
                print(results)
                return render_template("logged.html", results = results)



@app.route('/menu', methods=["GET","Post"])
def menu():
    if request.method == "POST":
        print ("hello")
        results = pizza.query.all()
        print (results)
        return render_template("menu.html", results = results)


@app.route('/cart', methods=["GET", "Post"])
def cart():
    if request.method == "POST":
        print (session['username'])
        print ("cart")
        id = request.form.get("pizzaid")
        print (id)
        pizz = customer()
        pizz.pizza_id = id
        db.session.add(pizz)
        db.session.commit()

@app.route('/admin', methods=["GET","Post"])
def admin():
    if request.method == "POST":
        
        
        return render_template("fail.html")

@app.route('/fail')
def fail():
    flash ("how the hell did you get here? ")
    return render_template("fail.html")




@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    customer = session['username']
    print (customer)
    update_customer = customer()

    update_customer.name = customer
    update_customer.active = False
    update_customer.pizza_id = None

    db.session.update(update_customer)
    print (update_customer)
    db.session.commit()

    results = customer.query.filter_by(name=user).first()    
    print(results)
    session.pop('username', None)
    return redirect(url_for('home'))

