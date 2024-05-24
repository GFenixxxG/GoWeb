from flask import Flask, request, url_for, render_template, redirect, session
import db_sripts

def startSession(quiz_id = 0):
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session["right_ans"] = 0
    session["wrong_ans"] = 0
    session["total"] = 0



app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
@app.route("/index")

def index():
    if request.method == "GET":
        startSession(-1)
        quizes_list = db_sripts.get_quizes()
        return render_template("index.html", quizes = quizes_list)

    else:
        quiz_id = request.form.get('quiz')
        print(quiz_id)
        return redirect(url_for('test'))

@app.route("/test", methods = ["GET", "POST"])
def test():
    return "<h1>Test Page</h1>"

@app.route("/result")
def result():
    return "<h1>result Page</h1>"

@app.route("/add_quiz")
def add_quiz():
    return "<h1>add_quiz Page</h1>"

app.config["SECRET_KEY"] = '00000000'

if __name__ == "__main__":
    app.run()