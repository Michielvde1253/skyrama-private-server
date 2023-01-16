import time
from pathlib import Path
import os
import json

def handle_ReturnPlane(request, user_id, json_data, task, task_number):
    if request["m"] == "planes.sendback":
        # To-do: Check for size + plane type!!!
        if task["obj_type_id"] == -1:
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
