import time
from pathlib import Path
import os
import json

def handle_placeableSetInStorage(request, user_id, rpcResult):
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

    if request["p"]["obj_type"] == "special":
      for i in json_data["specialBuildings"]:
        if int(i["id"]) == int(request["p"]["obj_id"]):
          i["position_x"] = request["p"]["x"]
          i["position_y"] = request["p"]["y"]
    elif request["p"]["obj_type"] == "bay":
      for i in json_data["bays"]:
        if int(i["id"]) == int(request["p"]["obj_id"]):
          i["position_x"] = request["p"]["x"]
          i["position_y"] = request["p"]["y"]
    elif request["p"]["obj_type"] == "runway":
      for i in json_data["runways"]:
        if int(i["id"]) == int(request["p"]["obj_id"]):
          i["position_x"] = request["p"]["x"]
          i["position_y"] = request["p"]["y"]
    elif request["p"]["obj_type"] == "landside_building":
      for i in json_data["landsideBuildings"]:
        if int(i["id"]) == int(request["p"]["obj_id"]):
          i["position_x"] = request["p"]["x"]
          i["position_y"] = request["p"]["y"]

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
