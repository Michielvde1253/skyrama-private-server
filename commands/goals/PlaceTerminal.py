import time
from pathlib import Path
import os
import json

def handle_PlaceTerminal(request, user_id, json_data, task, task_number):
    if request["m"] == "terminals.buy":
        if int(request["p"]["types_id"]) == int(task["obj_type_id"]):
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    return json_data
