import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_stories")
def get_stories():
    stories = list(mongo.db.stories.find())
    return render_template("stories.html", stories=stories)


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    stories = list(mongo.db.stories.find(
        {"created_by": username}))
    jokes = list(mongo.db.jokes.find({"created_by": username}))
    return render_template(
        "account.html", stories=stories, jokes=jokes, username=username)


@app.route("/get_jokes")
def get_jokes():
    jokes = list(mongo.db.jokes.find())
    return render_template("jokes.html", jokes=jokes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email-address": request.form.get("email-address"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("account", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "get_stories", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>")
def profile(username):
    username = mongo.db.users.find_one({"username": username})["username"]
    stories = list(mongo.db.stories.find(
        {"created_by": username}))
    jokes = list(mongo.db.jokes.find({"created_by": username}))
    return render_template(
        "profile.html", stories=stories, jokes=jokes, username=username)


@app.route("/story/<story_id>")
def story(story_id):
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    story_comment = list(
        mongo.db.story_comment.find({'story_id': story_id}))
    return render_template(
        "story.html", story=story, story_comment=story_comment)


@app.route("/add_story", methods=["GET", "POST"])
def add_story():
    if session.get("user", ""):
        if request.method == "POST":
            story = {
                "story_title": request.form.get("story_title"),
                "story_content": request.form.get("story_content"),
                "created_by": session["user"]
            }
            mongo.db.stories.insert_one(story)
            flash("Story Successfully Added")
            return redirect(url_for("get_stories"))

        return render_template("add_story.html")
    else:
        return render_template("register.html")


@app.route("/add_story_comment/<story_id>", methods=["GET", "POST"])
def add_story_comment(story_id):
    if request.method == "POST":
        story_comment = {
            "story_id": request.form.get("story_id"),
            "story_comment": request.form.get("story_comment"),
            "created_by": session["user"]
        }
        mongo.db.story_comment.insert_one(story_comment)
        flash("Comment Successfully Added")
        return redirect(url_for("get_stories"))


@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    if story.get("created_by") == session.get("user", ""):
        if request.method == "POST":
            submit = {
                "story_title": request.form.get("story_title"),
                "story_content": request.form.get("story_content"),
                "created_by": session["user"]
            }
            mongo.db.stories.update({"_id": ObjectId(story_id)}, submit)
            flash("Story Successfully Edited")

        return render_template("edit_story.html", story=story)
    else:
        return redirect(url_for("get_stories"))


@app.route("/delete_story/<story_id>")
def delete_story(story_id):
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    if story.get("created_by") == session.get("user", ""):
        mongo.db.stories.remove({"_id": ObjectId(story_id)})
        flash("Story Deleted")
        return redirect(url_for("get_stories"))
    else:
        return redirect(url_for("get_stories"))


@app.route("/joke/<joke_id>")
def joke(joke_id):
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})
    joke_comment = list(
        mongo.db.joke_comment.find({'joke_id': joke_id}))
    return render_template(
        "joke.html", joke=joke, joke_comment=joke_comment)


@app.route("/add_joke", methods=["GET", "POST"])
def add_joke():
    if session.get("user", ""):
        if request.method == "POST":
            joke = {
                "joke_title": request.form.get("joke_title"),
                "joke_content": request.form.get("joke_content"),
                "created_by": session["user"],
            }
            mongo.db.jokes.insert_one(joke)
            flash("Your joke has been added!")
            return redirect(url_for("get_jokes"))

        return render_template("add_joke.html")
    else:
        return render_template("register.html")


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})
    if joke.get("created_by") == session.get("user", ""):
        if request.method == "POST":
            submit = {
                "joke_title": request.form.get("joke_title"),
                "joke_content": request.form.get("joke_content"),
                "created_by": session["user"]
            }
            mongo.db.jokes.update({"_id": ObjectId(joke_id)}, submit)
            flash("Joke Successfully Edited")
        return render_template("edit_joke.html", joke=joke)
    else:
        return redirect(url_for("get_jokes"))


@app.route("/add_joke_comment/<joke_id>", methods=["GET", "POST"])
def add_joke_comment(joke_id):
    if session.get("user", ""):
        if request.method == "POST":
            joke_comment = {
                "joke_id": request.form.get("joke_id"),
                "joke_comment": request.form.get("joke_comment"),
                "created_by": session["user"]
            }
            mongo.db.joke_comment.insert_one(joke_comment)
            flash("Comment Successfully Added")
            return redirect(url_for("get_jokes"))
    else:
        return render_template("register.html")


@app.route("/delete_joke/<joke_id>")
def delete_joke(joke_id):
    joke = mongo.db.jokes.find_one(
        {"_id": ObjectId(joke_id)})
    if joke.get("created_by") == session.get("user", ""):
        mongo.db.jokes.remove({"_id": ObjectId(joke_id)})
        flash("Joke Deleted")
        return redirect(url_for("get_jokes"))
    else:
        return redirect(url_for("get_jokes"))


@app.route("/delete_joke_comment/<joke_comment_id>")
def delete_joke_comment(joke_comment_id):
    joke_comment = mongo.db.joke_comment.find_one(
        {"_id": ObjectId(joke_comment_id)})
    if joke_comment.get("created_by") == session.get("user", ""):
        mongo.db.joke_comment.remove({"_id": ObjectId(joke_comment_id)})
        flash("Joke Comment Deleted")
        return redirect(url_for("get_jokes"))
    else:
        return redirect(url_for("get_jokes"))


@app.route("/edit_joke_comment/<joke_comment_id>", methods=["GET", "POST"])
def edit_joke_comment(joke_comment_id):
    joke_comment = mongo.db.joke_comment.find_one(
        {"_id": ObjectId(joke_comment_id)})
    if joke_comment.get("created_by") == session.get("user", ""):
        if request.method == "POST":
            submit = {
                "joke_id": request.form.get("joke_id"),
                "joke_comment": request.form.get("joke_comment"),
                "created_by": session["user"]
            }
            mongo.db.joke_comment.update(
                {"_id": ObjectId(joke_comment_id)}, submit)
            flash("Joke Comment Successfully Edited")
        return render_template(
            "edit_joke_comment.html", joke_comment=joke_comment)
    else:
        return redirect(url_for("get_jokes"))


@app.route("/search_stories", methods=["GET", "POST"])
def search_stories():
    query = request.form.get("search")
    stories = list(mongo.db.stories.find({"$text": {"$search": query}}))
    return render_template("stories.html", stories=stories)


@app.route("/search_jokes", methods=["GET", "POST"])
def search_jokes():
    query = request.form.get("search")
    jokes = list(mongo.db.jokes.find({"$text": {"$search": query}}))
    return render_template("jokes.html", jokes=jokes)


@app.route("/delete_story_comment/<story_comment_id>")
def delete_story_comment(story_comment_id):
    story_comment = mongo.db.story_comment.find_one(
        {"_id": ObjectId(story_comment_id)})
    if story_comment.get("created_by") == session.get("user", ""):
        mongo.db.story_comment.remove({"_id": ObjectId(story_comment_id)})
        flash("Story Comment Deleted")
        return redirect(url_for("get_stories"))
    else:
        return redirect(url_for("get_stories"))


@app.route("/edit_story_comment/<story_comment_id>", methods=["GET", "POST"])
def edit_story_comment(story_comment_id):
    story_comment = mongo.db.story_comment.find_one(
        {"_id": ObjectId(story_comment_id)})
    if story_comment.get("created_by") == session.get("user", ""):
        if request.method == "POST":
            submit = {
                "story_id": request.form.get("story_id"),
                "story_comment": request.form.get("story_comment"),
                "created_by": session["user"]
            }
            mongo.db.story_comment.update(
                {"_id": ObjectId(story_comment_id)}, submit)
            flash("Story Comment Successfully Edited")
        return render_template(
            "edit_story_comment.html", story_comment=story_comment)
    else:
        return redirect(url_for("get_stories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
