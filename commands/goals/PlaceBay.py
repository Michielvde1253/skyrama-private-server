import time
from pathlib import Path
import os
import json

def handle_PlaceBay(request, user_id, json_data, task, task_number):
    if request["m"] == "placeable.place":
        if task["obj_type_id"] == -1 and request["p"]["obj_type"] == "bay":
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
