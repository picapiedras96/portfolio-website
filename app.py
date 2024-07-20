from flask import Flask, render_template, jsonify

app = Flask(__name__)  #instance of Flask object

# sample database using list
PROJECTS = [{
    'id':
    1,
    'title':
    'pedrothedev.com',
    'description':
    '   The website you are currently browsing is my first official project, initiated in May 2024. Balancing this project alongside my internship, I developed the site using Flask and incorporated various Python implementations. As my inaugural project, I’m excited to continue expanding the website with new ideas and experimental features.'
}]


@app.route("/")  #route/ sub address
def home():
  return render_template("home.html")


@app.route("/api/projectlistobjects")
def list_projects():
  return jsonify(PROJECTS)


@app.route("/projects")
def projects():
  return render_template("projects.html", projects=PROJECTS)


@app.route("/about")
def contact():
  return render_template("about.html")


if __name__ == "__main__":  #if this file is run directly perform action
  app.run("0.0.0.0", debug=True)  #run the app
