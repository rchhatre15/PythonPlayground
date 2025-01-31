from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import os
import requests

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Bootstrap5(app)

instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

db_path = os.path.join(instance_path, 'movies.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
print(f"Database path: {db_path}")  # Debug print
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(Text, nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

class EditMovieForm(FlaskForm):
    rating = FloatField('Your rating out of 10, eg. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


with app.app_context():
    try:
        db.create_all()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        db.session.rollback()

@app.route("/")
def home():
    try:
        all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
        return render_template("index.html", movies=all_movies)
    except Exception as e:
        print(f"Error in home route: {str(e)}")
        return f"An error occurred: {str(e)}"


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditMovieForm()
    if form.validate_on_submit():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    if 'search_results' in session:
        session.pop('search_results')
        
    form = AddMovieForm()
    if form.validate_on_submit():
        print("in with: ", form.title.data)
        url = "https://api.themoviedb.org/3/search/movie"
        
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZDA0MDQ0MzBjOGMyMzAzMjM3MWEyMDk5NDVjYmE0MCIsIm5iZiI6MTczODE4NjM1Ny4zMjUsInN1YiI6IjY3OWE5ZTc1MTI1Nzk4YWQ0YmJkNjkyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YiTtiEWSBjyN97TFp2zbKLDPWc6vKSk9IhanZEKQhh8"
        }

        params = {
            "query": form.title.data,
            "include_adult": "false",
            "language": "en-US",
            "page": "1"
        }

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                # print(data["results"])
                movies_data = [(movie["id"], movie["title"], movie["release_date"]) for movie in data["results"]]
                session['search_results'] = movies_data
                return redirect(url_for('select', movie_name=form.title.data))
            else:
                print("No movies found")    
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
        
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/select/<string:movie_name>", methods=["GET", "POST"])
def select(movie_name):
    if request.method == "GET":
        movies_data = session.get('search_results', [])
        return render_template("select.html", movies=movies_data)
    else:
        movie_id = request.form.get('movie_id')
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZDA0MDQ0MzBjOGMyMzAzMjM3MWEyMDk5NDVjYmE0MCIsIm5iZiI6MTczODE4NjM1Ny4zMjUsInN1YiI6IjY3OWE5ZTc1MTI1Nzk4YWQ0YmJkNjkyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YiTtiEWSBjyN97TFp2zbKLDPWc6vKSk9IhanZEKQhh8"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # print(data)
            db.session.execute(db.insert(Movie).values(id=data["id"], title=data["title"], year=data["release_date"][0:4], description=data["overview"], rating=None, ranking=None, review=None, img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"))
            db.session.commit()
            return redirect(url_for('edit', movie_id=data["id"]))
        else:
            print(f"Error: {response.status_code}")
            return redirect(url_for('add'))

if __name__ == '__main__':
    app.run(debug=True)
