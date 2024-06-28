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

def check_answer():
    answer = request.form.get("ans_name")
    quest_id  = request.form.get('q_id')
    session['last_question'] = quest_id
    session["total"] += 1
    if db_sripts.check_ans(answer, quest_id):
        session['right_ans'] += 1
    else:
        session['wrong_ans'] += 1

@app.route("/test", methods = ["GET", "POST"])
def test():
    #question = db_sripts.get_question_after(session['last_question'], session['quiz'])
    if not ("quiz" in session) and session['quiz'] < 0:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            check_answer()

        new_question = db_sripts.get_question_after(session["last_question"], session['quiz'])
        if new_question is None or len(new_question) == 0:
            return redirect(url_for('result'))
        else:
            return question_form(new_question)

            #return redirect("test")

@app.route("/result")
def result():
    res = render_template("result.html", total = session["total"], right = session['right_ans'], wrong = session["wrong_ans"])
    session.clear()
    return res

def save_quiz():
    quiz = request.form.get("quiz")
    question = request.form.getlist('question[]')
    db_sripts.insert_question(question)
    quizes = db_sripts.get_quizes()
    for id, name in quizes:
        if name.lower() == quiz.lower():
            db_sripts.add_link(quiz)
            break
    else:
        db_sripts.insert_quiz(quiz)
        db_sripts.add_link(quiz)


@app.route("/add_quiz", methods = ["GET", "POST"])
def add_quiz():
    if request.method == "GET":
        return render_template("add_quiz.html")
    else:
        save_quiz()
        return redirect(url_for("index"))

app.config["SECRET_KEY"] = '00000000'

if __name__ == "__main__":
    app.run()