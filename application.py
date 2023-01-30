from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def homepage():
    return render_template("homepage.html")