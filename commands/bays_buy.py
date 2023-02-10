import time
from pathlib import Path
import os
import json

def handle_baysBuy(request, user_id, rpcResult):
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

    json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - request["p"]["influenceableType"]["air_coins_cost"]
    json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - request["p"]["influenceableType"]["event_currency_cost"]
            
    json_data["bays"].append({"bay_types_id": request["p"]["types_id"],"last_harvest_time": request["p"]["last_harvest_time"],"set_in_storage_time": request["p"]["set_in_storage_time"],"id": json_data["playerData"]["next_object_id"],"position_x": request["p"]["position_x"],"position_y": request["p"]["position_y"],"direction": request["p"]["direction"],"player_id": user_id})
            
    json_data["playerData"]["next_object_id"] = int(json_data["playerData"]["next_object_id"]) + 1

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
