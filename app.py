from flask import Flask, render_template, jsonify

app = Flask(__name__)  #instance of Flask object

# sample database using list
PROJECTS = [{
    'id':
    1,
    'title':
    'pedrothedev.com',
    'description':
    '   The website you are currently browsing on is my first official launched project. I decided to create this website in May 2024 as an opportuinity to apply and display my development skills. I decided to implement the website with flask as it was an opportunity to use Python on my project one of my favorite languages. The domain "pedrothedev.com" came into existance with the idea to title my page "Vote for Pedro", sadly this domain was already taken and not worth the price. In this site you will find various implementations of CSS and HTML as well as some Python. My end goal for this site is to create a presense as I grow and develop more projects, this site is a continous project and will have future updates as I test new ideas.'
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


@app.route("/contact")
def contact():
  return render_template("contact.html")


if __name__ == "__main__":  #if this file is run directly perform action
  app.run("0.0.0.0", debug=True)  #run the app
