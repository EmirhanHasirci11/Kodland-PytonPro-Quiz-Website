from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models import db, User, Question

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "kodlandsecretkey"

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def landing():
    questions = Question.query.all()
    highest_score = db.session.query(func.max(User.score)).scalar() or 0  # Genel en yüksek skor

    if request.method == "POST":
        # Eğer kullanıcı session'da kayıtlıysa
        if "user" in session and request.form.get("username").strip() == session["user"]:
            username = session["user"]
        else:
            # Yeni kullanıcı, formdan gelen isim
            form_name = request.form.get("username").strip()
            existing_user = User.query.filter_by(username=form_name).first()

            # Aynı kullanıcı başka cihazda mı açık?
            if existing_user:
                return render_template("landing.html", username=None, score=None, questions=questions, highest_score=highest_score, error="Bu kullanıcı adı başka bir cihazda kullanımda.")


            # Yeni kullanıcı kaydı
            new_user = User(username=form_name)
            db.session.add(new_user)
            db.session.commit()
            session["user"] = form_name
            username = form_name

        # Quiz cevapları kontrol
        correct_count = 0
        for question in questions:
            selected = request.form.get(f"q{question.id}")
            if selected and selected.upper() == question.correct_option.upper():
                correct_count += 1

        score_percent = int((correct_count / len(questions)) * 100)

        # Skoru güncelle (eğer yeniyse)
        user = User.query.filter_by(username=username).first()
        if user and score_percent > user.score:
            user.score = score_percent
            db.session.commit()

        return render_template("landing.html", username=user.username, score=user.score,
                               questions=questions, submitted=True, correct=score_percent,
                               highest_score=highest_score)

    # GET isteği
    user = None
    score = None
    if "user" in session:
        user = User.query.filter_by(username=session["user"]).first()
        if user:
            score = user.score

    return render_template("landing.html", username=session.get("user"), score=score,
                           questions=questions, highest_score=highest_score)

@app.route("/logout")
def logout():
    return redirect("/")

with app.app_context():
    db.create_all()
