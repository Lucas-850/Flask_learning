from flask import Flask 
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "index page"

@app.route("/hello")
def hello():
    return f"Hello!"





if __name__ == '__main__':
    app.run(debug=True)