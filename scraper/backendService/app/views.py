from app import app
from app import r
from app import q

from flask import render_template, request


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    return render_template("add_task.html")