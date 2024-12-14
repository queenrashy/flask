from flask import Flask , render_template

app = Flask(__name__)

#create a route decorator

@app.route('/')

def index():
    first_name = "queen"
    stuff = "This is  bold  text "

    favorite_pizza = ["rice", "bean", "ewa" ,41]
    return render_template("index.html" , first_name=first_name , stuff =stuff ,favorite_pizza=favorite_pizza)

#  localhost:5000/user/queen

@app.route('/user/<name>')

def user(name):
     return render_template("user.html" , user_name=name)

# create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404
# internal server error URL 

@app.errorhandler(500)
def page_not_found(e):
     return render_template("500.html"), 500