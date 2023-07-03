import time
from pathlib import Path
import os
import json

def handle_LandPlane(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "planes.setState":
        # 1005 = landed, plane still on runway (own plane)
        # 105 = landed, plane still on runway (buddy plane)
        if request["p"]["flight_status"] == 105 or request["p"]["flight_status"] == 1005:
            for i in json_data["planes"]:
                if int(i["id"]) == int(request["p"]["id"]):
                    type_id = int(i["plane_type_id"])
                    break
            if int(task["obj_type_id"]) == type_id or int(task["obj_type_id"]) == -1:
                json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] + 1
    
    return json_data
