from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 

# use uuid to generate unique id in python
# To send api, use jsonify from flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(20), nullable=False, default="N/A")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.title) + '\nBy: ' + str(self.id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        post= request.form
        post = BlogPost(title=post['title'], content=post['content'], author=post['author'])
        db.session.add(post)
        db.session.commit()

        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date).all()
        return render_template("posts.html", posts=all_posts)

@app.route("/users/<string:name>")
def hello(name):
    return "Hello, " + name

@app.route('/onlyget', methods=['GET'])
def get_req():
    return "You can only use get method for this webpage"

if __name__ == "__main__":
    app.run(debug=True)
