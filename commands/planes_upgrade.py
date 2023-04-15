import time
from pathlib import Path
import os
import json
import copy

def handle_planesUpgrade(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None
    items_to_add_to_obj.append("planes")
    items_to_add_to_obj.append("planeUpgrades")
    items_to_add_to_obj.append("consumables")
    
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

    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
          i["upgrade_level"] = i["upgrade_level"] + 1
          current_upgrade_number = i["upgrade_level"]
          current_plane_type_id = i["plane_type_id"]
                
          for j in init_data["planeUpgradeTypes"]:
            if init_data["planeUpgradeTypes"][j]["level"] == current_upgrade_number:
              if current_plane_type_id in init_data["planeUpgradeTypes"][j]["attachableTo"]:
                upgrade_type = j
                for g in init_data["planeUpgradeTypes"][j]["effects"]:
#                  if g["type"] == "flight_time": # Not needed :)
#                    i["departure_time"] = str(int(time.time()) - ((i["arrival_time"] - i["departure_time"]) * (1 - (g["percent"] / 100)))) # Might get broken with turbo fuel
#                    i["arrival_time"] = str(int(time.time()))
                    
                    if g["type"] == "xp":
                      i["xp"] = i["xp"] * (1 + (g["percent"] / 100))
                      
                    if g["type"] == "air_coins":
                      i["air_coins"] = i["air_coins"] * (1 + (g["percent"] / 100))
                      
                    if g["type"] == "cargo":
                      i["wares_revenue"] = i["wares_revenue"] * (1 + (g["percent"] / 100))
          
          break
        
    for i in init_data["planeUpgradeCostTypes"]:
      if current_plane_type_id in i["planeIds"]:
        for j in i["costs"][str(current_upgrade_number)]:
          print(j)
          if j["type"] == "consumable": # Reduce tuning parts
            json_data["consumables"][j["id"]] = json_data["consumables"][j["id"]] - j["amount"]
            
          if j["type"] == "currency": # Not checking for id, as only coins are possible?
            json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - j["amount"]
        break
      
    # Add upgrade to planeUpgrades. For some reason this is during init not being sent in rpcResults, but in Object???
    if not "planeUpgrades" in json_data:
      json_data["planeUpgrades"] = {} # First upgrade: initialize json_data
      
    if not str(request["p"]["id"]) in json_data["planeUpgrades"]: # First upgrade on plane
      json_data["planeUpgrades"][str(request["p"]["id"])] = []
    
    json_data["planeUpgrades"][str(request["p"]["id"])].append(int(upgrade_type))

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
