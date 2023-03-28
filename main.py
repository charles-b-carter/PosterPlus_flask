from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login.html")
def login():
    return render_template('login.html')


@app.route("/register.html")
def register():
    return render_template('register.html')


@app.route("/JudgeGrading.html")
def JudgeGrading():
    return render_template('JudgeGrading.html')


@app.route("/JudgeLanding.html")
def JudgeLanding():
    return render_template('JudgeLanding.html')


@app.route("/Rubric.html")
def Rubric():
    return render_template('Rubric.html')


@app.route("/StudentLanding.html")
def StudentLanding():
    return render_template('StudentLanding.html')


@app.route("/TopScores.html")
def TopScores():
    return render_template('TopScores.html')


if __name__ == "__main__":
    app.run()
