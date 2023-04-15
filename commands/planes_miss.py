import time
from pathlib import Path
import os
import json

def handle_planesMiss(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}
    rpcResult["r"]["planes"] = {}


    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()

    if request["p"]["id"] != 0:
      j = 0
      for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
          json_data["planes"].pop(j)
        j = j + 1


    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()