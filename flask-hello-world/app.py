#---Flask Hello World app---#

#import class Flask from flask package
from flask import Flask

#create app object from instance of Flask class
app = Flask(__name__)

#link the view function to a url
@app.route("/")
@app.route("/hello")

#define the view
def hello_world():
    return "Hello, world!"

#launch the dev server on port 5000 --> go to localhost:5000 to see the app running
if __name__ == "__main__":
    app.run()