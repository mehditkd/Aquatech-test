from flask import Flask, request
from flask_cors import CORS
from Services.Tank import Tank as TankService
from Utils.Decorator.Json import json_response

app = Flask(__name__)
CORS(app)

tankService = TankService()

@app.route("/api/ping")
def ping():
    return "pong"

@app.route("/api/data")
@json_response
def get_data_route():
    min_date = request.args.get("min_date")
    max_date = request.args.get("max_date")
    return tankService.get(min_date, max_date)