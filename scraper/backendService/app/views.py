from app import app
from app import r
from app import q
from app import ratingscrape
from flask import render_template, request


@app.route("/task/<userurl>")
def task():
    

    job = q.enqueue(ratingscrape.getRatings, userurl)

    return f"Task ({job.id}) added to queue at {job.enqueued_at}"

