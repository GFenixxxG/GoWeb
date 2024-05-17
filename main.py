from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route("/index")

def index():
    return "<h1>Start Page</h1>"

@app.route("/test")
def test():
    return "<h1>Test Page</h1>"

@app.route("/result")
def result():
    return "<h1>result Page</h1>"

@app.route("/add_quiz")
def add_quiz():
    return "<h1>add_quiz Page</h1>"

if __name__ == "__main__":
    app.run()