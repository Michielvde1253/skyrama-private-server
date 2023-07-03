import time
from pathlib import Path
import os
import json

def handle_CollectSouvenir(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "planes.takeMeans":
        if "souvenir_types_id" in request["p"]:
            if int(task["obj_type_id"]) == int(request["p"]["souvenir_types_id"]):
                json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
