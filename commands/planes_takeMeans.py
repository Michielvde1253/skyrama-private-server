import time
from pathlib import Path
import os
import json

def handle_planesTakeMeans(request, user_id, rpcResult, items_to_add_to_obj):
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

    j = 0
    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["plane_id"]:
            plane_type_id = int(i["plane_type_id"])
            for g in init_data["planeTypes"]:
                if int(g["id"]) == plane_type_id:
                    service_time = g["service_length"]
                    quick_start_coins_cost = g["quick_start_coins_cost"]
                    quick_buddy_serve_coins_cost = g["quick_buddy_serve_coins_cost"]
                    
                    if "air_coins" in request["p"]:
                      json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] + request["p"]["air_coins"]
                      
                    if "xp" in request["p"]:
                      json_data["playerData"]["xp"] = json_data["playerData"]["xp"] + request["p"]["xp"]
                    
                    if "buddy_points" in request["p"]:
                      for h in json_data["buddyStuff"]["buddies"]:
                        if int(request["p"]["owner_id"]) == int(user_id):
                          if int(h["hi_player_id"]) == int(i["to_player_id"]):
                            h["buddy_points"] = int(h["buddy_points"]) + int(request["p"]["buddy_points"])
                        else:
                          if int(h["hi_player_id"]) == int(i["player_id"]):
                            h["buddy_points"] = int(h["buddy_points"]) + int(i["buddy_points"])
                    # To-do: Cargo planes
                    
                    if "souvenir_types_id" in request["p"]:
                      for h in json_data["souvenirCollections"]:
                        for k in h["items"]:
                            if int(k["type_id"]) == int(request["p"]["souvenir_types_id"]):
                              k["num"] = int(k["num"]) + 1
                    break


            # CHECK IF QUICK SERVICE IS USED
            # To-do: properly test if this works

            if int(request["p"]["owner_id"]) == int(user_id) and "xp" in request["p"]:
                if "xp" in request["p"]: # Add xp as temporary fix. This should be moved to planes.setState to avoid that.
                  if (int(request["t"]) - int(i["start_service_time"])) < (int(service_time) / 3) or int(i["start_service_time"]) == 0: # Own plane
                    json_data["playerData"]["air_cash"] = int(json_data["playerData"]["air_cash"]) - int(quick_start_coins_cost)   

            elif int(request["p"]["owner_id"]) != int(user_id):
              if ("xp" in request["p"]) or int(request["p"]["plane_id"]) == 0: # Add xp as temporary fix. This should be moved to planes.setState to avoid that. Plane id 0 = Cashcow
                if (request["t"] - i["start_service_time"]) < service_time or i["start_service_time"] == 0: # Buddy plane
                     json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - quick_buddy_serve_coins_cost


        j = j + 1

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
