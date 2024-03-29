from flask import Flask

app = Flask(__name__)  #instance of Flask object


@app.route("/")  #route/ sub address
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == "__main__":  #if this file is run directly perform action
  app.run("0.0.0.0", debug=True)  #run the app
