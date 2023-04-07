
from flask import Flask,render_template


app = Flask(__name__)


@app.route("/")

 
def first_flask():

    name = "Aarav"
    age="14"
    rel = "Me"
    img = "flask.jpg"
    return render_template("me.html", name = name, age=age,rel = rel, img = img )

@app.route("/father")
def second_flask():
     name = "Sanjay"
     age=40
     rel = "Father"
     

     return render_template('father.html', name = name, age=age,rel = rel  )

@app.route("/Mother")
def third_flask():
     name = "Teena"
     age=35
     rel = "Mother"
  
     return render_template('mother.html', 
                            name = name, age=age,rel = rel 
 )

@app.route("/friend")
def four_flask():
     name = "Harry"
     age=13
     rel = "Friend"

     return render_template('friend.html', 
                            name = name, age=age,rel = rel 
 )

app.run(debug=True)