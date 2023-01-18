import time
from pathlib import Path
import os
import json

def handle_landside_buildingsHarvest(request, user_id, rpcResult):
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

    f = open(os.path.join(p, "data", "global_init_data.json"), "r")
    init_data = json.loads(str(f.read()))
    f.close()


    if request["p"]["obj_type"] == "terminal":
        j = 0
        for i in json_data["terminals"]:
            if int(i["id"]) == request["p"]["id"]:
                json_data["terminals"][j]["last_harvest_time"] = request["p"]["last_harvest_time"]
                terminal_types_id = json_data["terminals"][j]["terminal_types_id"]
                for g in init_data["terminalTypes"]:
                    if int(g["id"]) == int(terminal_types_id):
                        num_received_passengers = g["capacity"]
                json_data["playerData"]["passengers"] = json_data["playerData"]["passengers"] + num_received_passengers
                request["p"]["num_received_passengers"] = num_received_passengers # Simplify the GetPassengers quest script.
            j = j + 1
    
# To-do: add landside buildings

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
