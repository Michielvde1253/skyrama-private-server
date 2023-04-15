import time
from pathlib import Path
import os
import json

def handle_specialBuildingsBuy(request, user_id, rpcResult, items_to_add_to_obj):
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

    for i in init_data["specialBuildingTypes"]:
      if int(i["id"]) == int(request["p"]["types_id"]):
        json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - i["air_coins_cost"]
        json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - i["air_cash_cost"]
        json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - i["event_currency_cost"]
            
        json_data["specialBuildings"].append({"sbId":"1","special_building_types_id":request["p"]["types_id"],"id":json_data["playerData"]["next_object_id"],"position_x":request["p"]["position_x"],"position_y":request["p"]["position_y"],"direction":request["p"]["direction"],"player_id":user_id})
        # What is sbId??? Doesn't seem to matter for now
    
        json_data["playerData"]["next_object_id"] = int(json_data["playerData"]["next_object_id"]) + 1

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
