import time
from pathlib import Path
import os
import json

def handle_goalsBuyTask(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None
    
    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()  

    current_goal = json_data["goals"]["goals"][request["p"]["seq_type"]]

    for task in current_goal["tasks"]:
        num_checks = 0
        if task["user_action"] == request["p"]["user_action"]:
            if type(task["obj_type_id"]) == type(request["p"]["obj_type_id"]):
                if task["obj_type_id"] == request["p"]["obj_type_id"]:
                    num_checks += 1
            if type(task["location_id"]) == type(request["p"]["location_id"]):
                if task["location_id"] == request["p"]["location_id"]:
                    num_checks += 1
            if type(task["plane_type"]) == type(request["p"]["plane_type"]):
                if task["plane_type"] == request["p"]["plane_type"]:
                    num_checks += 1
            if type(task["size"]) == type(request["p"]["size"]):
                if task["size"] == request["p"]["size"]:
                    num_checks += 1
            if type(task["continent"]) == type(request["p"]["continent"]):
                if task["continent"] == request["p"]["continent"]:
                    num_checks += 1

            if num_checks == 5:
                # We checked everything we could, 99% sure it's the correct task xD (why doesn't the client just send the id???)
                # There was an issue in new_player.json that caused the first quest to have None as air_cash_cost. Old account: just complete first quest manually :)

                task["num_completed"] = task["num_required"]
                air_cash_cost = task["air_cash_cost"]
                json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - air_cash_cost

                # Just let the next quest being started by the regular quest script.
    
    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()