import time
from pathlib import Path
import os
import json

def handle_buddyGetAll(request, user_id, rpcResult):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}


    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()

    rpcResult["r"]["buddies"] = json_data["buddyStuff"]["buddies"]
    rpcResult["r"]["packets"] = json_data["buddyStuff"]["packets"]
