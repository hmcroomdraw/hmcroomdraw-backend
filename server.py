from markupsafe import escape
from dataclasses import asdict
from flask import Flask, jsonify

from models import *

app = Flask(__name__)

@app.route('/login')
def login():
    user = User(
        id="USERID",
        first_name="Santi",
        last_name="Santichaivekin",
        email="jsantichaivekin@g.hmc.edu",
        class_year="senior",
        priority_number=1,
        gender="male",
    )
    return asdict(user)

@app.route('/display/residence-halls')
def get_residence_halls():
    all_residence_halls = ["drinkward", "linde"]
    return jsonify(all_residence_halls)

@app.route('/capitalize/<word>/')
def capitalize(word):
    raise NotImplementedError()
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

if __name__ == "__main__":
    app.run()