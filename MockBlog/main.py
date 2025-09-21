from flask import Flask, render_template, url_for
import requests

api_endpoint = "https://api.npoint.io/84bc2ded356d7eb9ffbb"

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(api_endpoint)
    data = response.json()
    header_url = url_for("static", filename="assets/img/home-bg.jpg")
    return render_template("index.html", data=data, header_url=header_url)

@app.route("/about")
def about():
    header_url = url_for("static", filename="assets/img/about-bg.jpg")
    return render_template("about.html", header_url=header_url)

@app.route("/post")
def post():
    header_url = url_for("static", filename="assets/img/post-bg.jpg")
    return render_template("post.html", header_url=header_url)

@app.route("/contact")
def contact():
    header_url = url_for("static", filename="assets/img/contact-bg.jpg")
    return render_template("contact.html", header_url=header_url)

@app.route("/show_post/<int:id>")
def show_post(id):
    header_url = url_for("static", filename="assets/img/post-sample-bg.jpg")
    response = requests.get(api_endpoint)
    data = response.json()
    curr_post = data[id - 1]
    return render_template("show_post.html", post=curr_post, header_url=header_url)


if __name__ == "__main__":
    app.run(debug=True)
