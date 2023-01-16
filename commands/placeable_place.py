import time
from pathlib import Path
import os
import json

def handle_placeablePlace(request, user_id, rpcResult):
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

    if request["p"]["obj_type"] == "bay":
        j = 0
        for i in json_data["bays"]:
            if int(i["id"]) == int(request["p"]["obj_id"]):
                json_data["bays"][j]["position_x"] = request["p"]["x"]
                json_data["bays"][j]["position_y"] = request["p"]["y"]
            j = j + 1

            print(json_data["bays"])

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
