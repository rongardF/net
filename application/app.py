from flask import Flask, render_template, request
from .models import create_post, get_posts

app=Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method=="POST":
        # get user input data from form
        name=request.form.get("name")
        post=request.form.get("post")
        # create new entry in DB
        create_post(name, post)
    
    posts=get_posts() # get all entries from table
    
    return render_template("index.html", posts=posts)
