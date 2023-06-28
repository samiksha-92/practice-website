from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': "Bangalore,India",
    'Salary': "Rs.10,00,000"
  },
  {
    'id': 2,
    'title': "Front End Engineer",
    'location': "Fully Remote",
    'Salary': "Rs.20,00,000"
  },
  {
    'id': 3,
    'title': "Director of Marketing",
    'location': "Newyork, US",
    'Salary': "$10,00,000"
  },
  {
    'id': 4,
    'title': "Community Manager",
    'location': "San Francisco, US",
    'Salary': "$60,000"
  }
  
]


@app.route("/")
def sam_title():
  return render_template('home.html', jobs= JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug="True")
