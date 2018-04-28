#---Flask Hello World app---#

#import class Flask from flask package
from flask import Flask

#create app object from instance of Flask class
app = Flask(__name__)

app.config["DEBUG"] = True

#link the view function to a url
@app.route("/")
@app.route("/hello")

#define the view
def hello_world():
    return "Hello, world!"

@app.route("/test/<search_query>")

def search(search_query):
    return search_query

@app.route("/integer/<int:value>")

def int_type(value):
    print(value + 1)
    return "correct"

#launch the dev server on port 5000 --> go to localhost:5000 to see the app running
if __name__ == "__main__":
    app.run()