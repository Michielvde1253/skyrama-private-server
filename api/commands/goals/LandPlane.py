import time
from pathlib import Path
import os
import json

def handle_LandPlane(request, user_id, json_data, task, task_number):
    if request["m"] == "planes.setState":
        if task["obj_type_id"] == -1 and request["p"]["id"] == 0 and request["p"]["flight_status"] == 105:
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
