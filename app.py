from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        "title": "Post 1",
        "content": "This is the content of post 1. Lalalalala",
        "author": "Aron"
    },
    {
        "title": "Post 2",
        "content": "This is the content of post 2. Lalalalala"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts=all_posts)

@app.route("/users/<string:name>")
def hello(name):
    return "Hello, " + name

@app.route('/onlyget', methods=['GET'])
def get_req():
    return "You can only use get method for this webpage"

if __name__ == "__main__":
    app.run(debug=True)
