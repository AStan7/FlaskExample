from flask import Flask, redirect, url_for, render_template, request
application = Flask(__name__)

@application.route("/", methods=['GET', "POST"])
def homepage():
    return render_template("homepage.html")