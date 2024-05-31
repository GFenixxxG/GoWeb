from flask import Flask, request, url_for, render_template, redirect, session
import db_sripts
from random import shuffle

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
        startSession(quiz_id)
        print(quiz_id)
        return redirect(url_for('test'))

def question_form(question):
    answer_list = [
        question[2],
        question[3],
        question[4],
        question[5],
    ]
    shuffle(answer_list)
    return render_template("test.html", question_id = question[0], quest = question[1], ans_list = answer_list)


@app.route("/test", methods = ["GET", "POST"])
def test():
    new_question = db_sripts.get_question_after(session['last_question'], session['quiz'])
    if not ("quiz" in session) and session['quiz'] < 0:
        return redirect(url_for("index"))
    else:
        if request.method == "GET":
            print(new_question)
            print(session)
            return question_form(new_question)    

@app.route("/result")
def result():
    return "<h1>result Page</h1>"

@app.route("/add_quiz")
def add_quiz():
    return "<h1>add_quiz Page</h1>"

app.config["SECRET_KEY"] = '00000000'

if __name__ == "__main__":
    app.run()