from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
import os

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Make sure instance folder exists
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Configure SQLite database with absolute path
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

# Create the database tables
with app.app_context():
    try:
        # print("Creating database tables...")  # Debug print
        # db.drop_all()  # Clear existing tables
        db.create_all()
        # second_movie = Movie(
        #     title="Avatar The Way of Water",
        #     year=2022,
        #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        #     rating=7.3,
        #     ranking=9,
        #     review="I liked the water.",
        #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        # )
        # db.session.add(second_movie)
        # db.session.commit()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        db.session.rollback()

@app.route("/")
def home():
    try:
        all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
        return render_template("index.html", movies=all_movies)
    except Exception as e:
        print(f"Error in home route: {str(e)}")
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
