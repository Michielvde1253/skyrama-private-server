import time
from pathlib import Path
import os
import json

def handle_GetPassengers(request, user_id, json_data, task, task_number):
    if request["m"] == "landside_buildings.harvest":
        json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + request["p"]["num_received_passengers"]
    
    return json_data
