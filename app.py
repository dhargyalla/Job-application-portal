from flask_bootstrap import Bootstrap5
from flask import Flask, render_template,jsonify
app = Flask(__name__)

bootstrap = Bootstrap5(app)

jobs = [
    {
        'id': 1,
        'title': 'Data Engineer',
        'location': 'Sheffield',
        'Salary': '$60K - $100K',
        'Requirements': ['React','Javascript','Python','Maths']

    },
    {
        'id': 2,
        'title': 'Data Analysis',
        'location': 'London',
        'Salary': '$50K - $140K',
        'Requirements': ['React','Javascript','Python','Maths']
    },
    {
        'id': 3,
        'title': 'Project manager',
        'location': 'Leeds',
        'Salary': '$30K - $130K',
        'Requirements': ['SPSS','Excel','Certification','Maths']
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Manchester',
        'Salary': '$50K - $200K',
        'Requirements': ['React','Javascript','Python','Maths']
    },
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/jobopening')
def applyjob():
    return render_template('jobopening.html',jobs = jobs, company_name = 'technologia')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run()
