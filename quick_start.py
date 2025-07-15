from flask import Flask , url_for, request
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return "index page"

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    return "Login Page"

@app.route("/hello")
def hello(name="Lucas"):
    return f"Hello, World!"


@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile "

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




with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



if __name__ == '__main__':
    app.run(debug=True)