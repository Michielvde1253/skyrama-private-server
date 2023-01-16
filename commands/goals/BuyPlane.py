import time
from pathlib import Path
import os
import json

def handle_BuyPlane(request, user_id, json_data, task, task_number):
    if request["m"] == "planes.buy":
        if task["obj_type_id"] == request["p"]["typeId"]:
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
