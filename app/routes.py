import random
from flask import render_template

from app import app


def random_str(length):
    return "".join(["abcdefghijklmnopqrstxyz"[random.randint(0, 25)] for _ in range(length)]).capitalize()

@app.route("/")
def r_index():
    table = [0,0,3,7,8]
    number = random.randint(0,9999)
    tableNumber = [random.randint(0, 9999) for _ in range(64)]
    html_text = "<i>coucou</i>"
    return render_template(
        "index.html",
        random_value=number,
        table=table,
        tableNumber=tableNumber,
        fn=random_str,
        html_text=html_text,
        visual_table=[[random.randint(0, 9) for _ in range(8)] for line in range(8)]
    )

@app.route("/test")
def r_test():
    return "Coucou c'est un test !"
