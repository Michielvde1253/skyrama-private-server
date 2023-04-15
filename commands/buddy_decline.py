import time
from pathlib import Path
import os
import json
def handle_buddyDecline(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None
    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break
            
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(request["p"]["buddyId"]):
            player_to_remove_file = file
            break
            
    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()
    
    f = open(os.path.join(p, "data", player_to_remove_file), "r")
    json2_data = json.loads(str(f.read()))
    f.close()

    g = 0
    for i in json_data["buddyStuff"]["buddies"]:
      print(i["hi_player_id"])
      print(request["p"]["buddyId"])
      if str(i["hi_player_id"]) == str(request["p"]["buddyId"]) and str(i["lo_player_id"]) == str(user_id):
        json_data["buddyStuff"]["buddies"].pop(g)
      g = g + 1
    g = 0    
    for j in json2_data["buddyStuff"]["buddies"]:
      print(j["hi_player_id"])
      print(request["p"]["buddyId"])
      if str(j["lo_player_id"]) == str(request["p"]["buddyId"]) and str(j["hi_player_id"]) == str(user_id):
        json2_data["buddyStuff"]["buddies"].pop(g)
      g = g + 1
    
    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()

    f = open(os.path.join(p, "data", player_to_remove_file), "w")
    f.write(json.dumps(json2_data))
    f.close()