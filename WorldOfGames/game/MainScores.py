from flask import render_template, Blueprint

score_page = Blueprint("score", __name__)


@score_page.route('/')
def score_server():
    with open('Scores.txt') as file:
        score = file.read().strip()
    return render_template("home.html", score=score)
