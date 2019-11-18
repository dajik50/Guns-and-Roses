from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/lists')
def lists():
    return render_template("lists.html")


@app.route('/pics')
def pics():
    return render_template("pics.html")


@app.route('/send')
def send():
    return render_template("send.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)