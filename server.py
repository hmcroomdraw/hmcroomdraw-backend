from markupsafe import escape
from dataclasses import asdict
from flask import Flask, jsonify, url_for

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
    return jsonify(user)

@app.route('/display/residence-halls')
def get_residence_halls():
    all_residence_hall_ids = ["drinkward", "linde"]
    return jsonify(all_residence_hall_ids)

@app.route('/display/residence-hall/<string:residence_hall_id>/floors')
def get_residence_hall(residence_hall_id):
    room1 = Room(
        id="room1",
        residence_hall_name="drinkward",
        floor_number=1,
        suite=None,
        number=1,
    )
    room2 = Room(
        id="room2",
        residence_hall_name="drinkward",
        floor_number=1,
        suite=None,
        number=2,
    )
    floor1_image = Image(
        url=url_for('static', filename="drinkward_floor1.png", _external=True),
        width=2304,
        height=1370,
    )
    room1_coord = Coordinate(
        x=300,
        y=1000,
    )
    room2_coord = Coordinate(
        x=600,
        y=1000,
    )
    floor1_coordinates = {
        "room1": room1_coord,
        "room2": room2_coord,
    }
    floor1 = FloorPlan(
        id="drinkward-floor1",
        residence_hall_name="drinkward",
        floor_number=1,
        rooms=[room1, room2],
        image=floor1_image,
        room_coordinates=floor1_coordinates
    )
    residence_hall = ResidenceHall(
        id="drinkward",
        name="drinkward",
        floors=[floor1],
    )
    return jsonify(residence_hall)

@app.route("/display/user/<string:user_id>/get-available-rooms")
def get_available_room_ids(user_id):
    rooms_available_for_user_id = ["room1", "room2"]
    return jsonify(rooms_available_for_user_id)

@app.route("/display/room/<string:room_id>")
def display_room(room_id):
    room1 = Room(
        id="room1",
        residence_hall_name="drinkward",
        floor_number=1,
        suite=None,
        number=1,
    )
    return jsonify(room1)

if __name__ == "__main__":
    app.run()