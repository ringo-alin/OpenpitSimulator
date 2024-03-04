# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

map = {"map": [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]}

avatar = {"x": 0, "y": 0}

@app.get("/avatar")
def get_avator():
    global avatar
    avatar["x"] = (avatar["x"] + 1) % 2
    return jsonify(avatar)

@app.get("/map")
def get_map():
    return jsonify(map)

