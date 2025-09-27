from attr.setters import validate
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"
Bootstrap5(app)

class EditForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g. 6.4", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField("Movie Title ", validators=[DataRequired()])
    year = IntegerField("Year Released", validators=[DataRequired()])
    description = StringField("Enter a Description", validators=[DataRequired()])
    rating = FloatField("Enter a Rating", validators=[DataRequired()])
    ranking = IntegerField("Enter Ranking e.g. 5", validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField("Enter a Review", validators=[DataRequired()])
    img_url = StringField("Enter an Image URL", validators=[DataRequired()])
    submit = SubmitField("Done")

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    ranking: Mapped[int] = mapped_column(Integer, default=0.0)
    review: Mapped[str] = mapped_column(String)
    img_url: Mapped[str] = mapped_column(String(500))


    def __repr__(self):
        return f"<User(id={self.id}, title='{self.title}')>"


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    print(movies)
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_movie = Movie(title=form.title.data, year=form.year.data, description=form.description.data,
                          rating=form.rating.data, ranking=form.ranking.data, review=form.review.data,
                          img_url=form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect("/")
    return render_template("add.html", form=form)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    movie = Movie.query.get(id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
