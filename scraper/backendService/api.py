from flask import Flask
import ratingscrape
app = Flask(__name__)

@app.route("/url/<user>")
def hello(user):
    userlist = ratingscrape.getRatings(user)


@app.route("/")
def hello():
    return "hello world"
if __name__ == "__main__":
    app.run(host='0.0.0.0')