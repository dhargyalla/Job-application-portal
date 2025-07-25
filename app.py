from flask_bootstrap import Bootstrap5
from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///jobportal.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Jobs(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    salary_min: Mapped[int] = mapped_column(Integer, nullable=False)
    salary_max: Mapped[int] = mapped_column(Integer, nullable=False)
    currency: Mapped[str] = mapped_column(String(200), nullable=False)
    requirements: Mapped[str] = mapped_column(String(2000), nullable=False)
    descriptions: Mapped[str] = mapped_column(String(2000), nullable=False)


    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# # CREATE RECORD
# with app.app_context():
#     new_job = Jobs(title="Data Analysis", location="Sheffield", salary_min=19000,salary_max=550000,currency="£",requirements="Python, SQL, AWS, Tableau, R",descriptions="Responsible for building data pipelines and managing cloud infrastructure as well as anallysis data")
#     db.session.add(new_job)
#     db.session.commit()

bootstrap = Bootstrap5(app)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/jobopening')
def applyjob():
    openjobs = Jobs.query.all()
    return render_template('jobopening.html',jobs = openjobs, company_name = 'technologia')

# @app.route('/api/jobs')
# def list_jobs():
#     return jsonify(jobs)

if __name__ == '__main__':
    app.run()
