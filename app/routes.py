from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])

def say_hello_world():
    my_beautiful_world = "Hello world!"
    return my_beautiful_world

@hello_world_bp.route("/hello/JSON", methods=['GET'])

def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }