from flask import Flask , url_for, request, render_template
from werkzeug.utils import secure_filename
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return "index page"

@app.route('/login', methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return "Logged in successfully!"
        else:
            error = 'Invalid username/password'
    
    return render_template('login.html', error=error)

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person = name)


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

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f'/var/www/uploads/{secure_filename(f.filename)}')
    




with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



if __name__ == '__main__':
    app.run(debug=True)