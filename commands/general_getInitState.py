import time
from pathlib import Path
import os
import json
import datetime

def handle_getInitState(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    items_to_add_to_obj.append("consumablesTypes")
    items_to_add_to_obj.append("consumables")
    items_to_add_to_obj.append("packagesTypes")
    items_to_add_to_obj.append("planeUpgrades")
    items_to_add_to_obj.append("planeUpgradeTypes")
    items_to_add_to_obj.append("planeUpgradeCostTypes")
    
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

    json_data["playerData"]["session_start_time"] = int(time.time())

    if True: # NEW PLAYER, SET UP CASHCOW           TO BE FIXED!
        # To-do: Restart tutorial if not completed.
        json_data["planes"][0]["departure_time"] = int(time.time()) - 450
        json_data["planes"][0]["arrival_time"] = int(time.time()) + 450 

    rpcResult["r"] = {**json_data, **init_data} # Merge both global init and personal user init.

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
    