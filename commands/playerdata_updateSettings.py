import time
from pathlib import Path
import os
import json

def handle_updateSettings(request, user_id, rpcResult):
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

    json_data["playerData"]["quickservice_on"] = request["p"]["quickservice_on"]
    json_data["playerData"]["effects_on"] = request["p"]["effects_on"]
    json_data["playerData"]["sound_on"] = request["p"]["sound_on"]
    json_data["playerData"]["superfuel_on"] = request["p"]["superfuel_on"]
    json_data["playerData"]["animations_on"] = request["p"]["animations_on"]

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
