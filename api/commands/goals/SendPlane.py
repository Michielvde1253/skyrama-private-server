import time
from pathlib import Path
import os
import json

def handle_SendPlane(request, user_id, json_data, task, task_number):
    if request["m"] == "planes.send":
        p = Path(__file__).parents[2]
        conditions_completed = 0
        for i in json_data["planes"]:
            if i["id"] == request["p"]["id"]:
                plane_type_id = i["plane_type_id"]
                break
        if task["obj_type_id"] != -1:
            if task["obj_type_id"] == plane_type_id:
                conditions_completed = conditions_completed + 1
        else:
            conditions_completed = conditions_completed + 1
        
        print(task["size"])
        if task["size"] != None:
            f = open(os.path.join(p, "data", "global_init_data.json"), "r")
            init_data = json.loads(str(f.read()))
            f.close()

            for i in init_data["planeTypes"]:
                if i["id"] == plane_type_id:
                    plane_size = i["size"]

            if task["size"] == plane_size:
                conditions_completed = conditions_completed + 1
        else:
            conditions_completed = conditions_completed + 1

        
        # TO-DO: Plane type check, location id check, continent check, ...
        print(conditions_completed)
        if conditions_completed == 2:
            json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] = json_data["goals"]["goals"]["main"]["tasks"][task_number]["num_completed"] + 1


#        if int(task["goal_types_id"]) == 4: # Tutorial, speed up Cashcow
#            json_data["planes"][0]["departure_time"] = int(time.time()) - 0
#            json_data["planes"][0]["arrival_time"] = int(time.time()) + 150


    return json_data
