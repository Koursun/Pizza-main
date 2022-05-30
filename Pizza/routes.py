from Pizza import app
from Pizza.models import pizza, Customer_Order
from flask import Flask, render_template

@app.route('/', methods=["GET","Post"])
def home():
    if request.method == "POST":
        print(saj)


    return render_template("home.html")




@app.route('/fail')
def fail():
    return render_template("fail.html")



