import time
from pathlib import Path
import os
import json

def handle_landsideBuildingsBuy(request, user_id, rpcResult, items_to_add_to_obj):
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
    
    landside_building = {}
    landside_building["landside_building_types_id"] = request["p"]["types_id"]
    landside_building["last_harvest_time"] = request["p"]["last_harvest_time"]
    landside_building["set_in_storage_time"] = request["p"]["set_in_storage_time"]
    landside_building["id"] = request["p"]["id"]
    landside_building["position_x"] = request["p"]["position_x"]
    landside_building["position_y"] = request["p"]["position_y"]
    landside_building["direction"] = request["p"]["direction"]
    landside_building["player_id"] = user_id

    json_data["landsideBuildings"].append(landside_building)
    
    # CHECK IF THE BUILDING IS ALREADY UNLOCKED
    # If yes: only use air coins, else only use air cash!!!
    for i in init_data["store_items"]["storeItems"]:
      if i["obj_type"] == "Landside_Building":
        if int(i["obj_type_id"]) == int(request["p"]["types_id"]):
          unlock_lvl = int(i["required_level"])
          break
      
    # Check current level based on xp
    current_xp = int(json_data["playerData"]["xp"])
    current_level = 100 # Handle the edge case when you're at the last level
    j = 0
    for i in json_data["playerData"]["xp_level_caps"]:
      if int(i) > current_xp:
        current_level = j
        break
      j = j + 1

    if request["p"]["influenceableType"]["air_coins_cost"] != 0:
      if current_level >= unlock_lvl:
        request["p"]["influenceableType"]["air_cash_cost"] = 0
      else:
        request["p"]["influenceableType"]["air_coins_cost"] = 0
        
    json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - request["p"]["influenceableType"]["air_coins_cost"]
    json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - request["p"]["influenceableType"]["air_cash_cost"]
    json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - request["p"]["influenceableType"]["event_currency_cost"]

    json_data["playerData"]["next_object_id"] = int(json_data["playerData"]["next_object_id"]) + 1
    
    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
