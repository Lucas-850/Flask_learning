from flask import Flask 
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "index page"

@app.route("/hello")
def hello(name="Lucas"):
    return f"Hello, World!"


@app.route('/user/<username>')
def show_user_profile(username):
    return f'user {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath: {escape(subpath)}"

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about")
def about():
    return "The about page" 


if __name__ == '__main__':
    app.run(debug=True)