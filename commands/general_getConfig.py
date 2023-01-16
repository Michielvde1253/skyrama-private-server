import time
from pathlib import Path
import os
import json

def handle_getConfig(request, user_id, rpcResult):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))

    print(user_id)
    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()

    rpcResult["r"] = {"viewportWidth":1000,"viewportHeight":600,"cellSize":24,"numCells":40,"cameraAngle":60,"userIdTest":user_id,"nextObjectId":json_data["playerData"]["next_object_id"],"serverTime":str(int(time.time())),"delta_ping":1800,"sort_buddylist":False,"event_basket_timeout":21600}