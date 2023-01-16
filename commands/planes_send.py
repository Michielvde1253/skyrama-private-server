import time
from pathlib import Path
import os
import json

def handle_planesSend(request, user_id, rpcResult):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}
    rpcResult["r"]["planes"] = {}


    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()

    j = 0
    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
            json_data["planes"][j]["departure_time"] = request["p"]["departure_time"]
            json_data["planes"][j]["contents_count"] = request["p"]["contents_count"]
            json_data["planes"][j]["kerosene_boost_flag"] = request["p"]["kerosene_boost_flag"]
            json_data["planes"][j]["last_state_change_time"] = request["p"]["last_state_change_time"]
            json_data["planes"][j]["subcontainer_id"] = request["p"]["subcontainer_id"]
            json_data["planes"][j]["container_id"] = request["p"]["container_id"]
            json_data["planes"][j]["arrival_time"] = request["p"]["arrival_time"]  
            json_data["planes"][j]["flight_status"] = 77

            rpcResult["r"]["planes"][str(request["p"]["id"])] = json_data["planes"][j]
        j = j + 1

    if True: # NEW PLAYER, SET UP CASHCOW
        json_data["planes"][0]["departure_time"] = int(time.time())
        json_data["planes"][0]["arrival_time"] = int(time.time()) + 150

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
