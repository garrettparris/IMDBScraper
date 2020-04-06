from flask import Flask
import ratingscrape
app = Flask(__name__)

@app.route("/analysis/<user>")
def hello(user):
    userlist = ratingscrape.getRatings(user)

if __name__ == "__main__":
    app.run(host='0.0.0.0')