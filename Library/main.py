from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

all_books = []


@app.route('/')
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    rating = request.form.get("rating")
    all_books.append({"title":title, "author": author, "rating": rating})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

