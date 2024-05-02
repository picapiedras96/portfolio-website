from flask import Flask, render_template, jsonify

app = Flask(__name__)  #instance of Flask object

# sample database using list
PROJECTS = [
    {
        'id': 1,
        'title': 'Personal Website',
        'description': '    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
]


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
