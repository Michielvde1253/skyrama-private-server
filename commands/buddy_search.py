import time
from pathlib import Path
import os
import json

def handle_buddySearch(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = []


    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[8:len(file)-5].lower().startswith(request["p"]["username"].lower()):
            friendship = "none"
            if file[0:8] == str(user_id):
              friendship = "yourself"
            else:
              f = open(os.path.join(p, "data", file), "r")
              json_data = json.loads(str(f.read()))
              f.close()
              for i in json_data["buddyStuff"]["buddies"]:
                if int(i["hi_player_id"]) == int(user_id):
                  friendship = "friend"
            rpcResult["r"].append({"player_id":file[0:8],"username":file[8:len(file)-5],"friendship":friendship})
