from flask import Flask, render_template
import requests


app = Flask(__name__)
api_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(api_endpoint)
data = response.json()
blogs = [item for item in data]

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route("/post/<int:id>")
def post(id):
    for blog in blogs:
        if blog['id'] == id:
            post = blog
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
