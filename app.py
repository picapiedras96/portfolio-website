from flask import Flask, render_template

app = Flask(__name__)  #instance of Flask object


@app.route("/")  #route/ sub address
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":  #if this file is run directly perform action
  app.run("0.0.0.0", debug=True)  #run the app
