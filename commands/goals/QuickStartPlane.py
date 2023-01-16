import time
from pathlib import Path
import os
import json

def handle_QuickStartPlane(request, user_id, json_data, task, task_number):
    if request["m"] == "planes.takeMeans":
        if request["p"]["plane_id"] == 0: # There's only one mission of this type, do it the lazy way.
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
