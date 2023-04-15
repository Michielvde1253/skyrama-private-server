import time
from pathlib import Path
import os
import json
import random

def handle_planesSend(request, user_id, rpcResult, items_to_add_to_obj):
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
    
    f = open(os.path.join(p, "data", "global_init_data.json"), "r")
    init_data = json.loads(str(f.read()))
    f.close()    

    player_to_file = 0
    j = 0
    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
            json_data["planes"][j]["departure_time"] = request["p"]["departure_time"]
            json_data["planes"][j]["contents_count"] = request["p"]["contents_count"]
            json_data["planes"][j]["kerosene_boost_flag"] = request["p"]["kerosene_boost_flag"]
            json_data["planes"][j]["last_state_change_time"] = request["p"]["last_state_change_time"]
            json_data["planes"][j]["subcontainer_id"] = request["p"]["subcontainer_id"]
            json_data["planes"][j]["container_id"] = request["p"]["container_id"]
            json_data["planes"][j]["arrival_time"] = request["p"]["arrival_time"]  
            json_data["planes"][j]["flight_status"] = 77
            json_data["planes"][j]["from_user_name"] = json_data["playerData"]["user_name"]
            json_data["planes"][j]["from_location_id"] = json_data["playerData"]["location_id"]
            json_data["planes"][j]["buddy_points"] = 0
            json_data["planes"][j]["fromUser_objectId"] = int(i["id"])
            
            for g in json_data["locations"]:
              if int(g["id"]) == int(json_data["planes"][j]["to_location_id"]):
                souvenirNum = random.randint(1,3)
                souvenir = g["souvenir_types_id_" + str(souvenirNum)]
                json_data["planes"][j]["souvenir_types_id"] = souvenir # To-do: event currency drop (= -2 ???)
                
            plane_type_id = int(i["plane_type_id"])
            for g in init_data["planeTypes"]:
                if int(g["id"]) == plane_type_id:
                    service_time = g["service_length"]
                    quick_start_coins_cost = g["quick_start_coins_cost"]
                    buddy_points = int(g["buddy_points_yield"])
                    
            print(int(request["t"]) - int(i["start_service_time"]))
            print(int(i["start_service_time"]))
            if (int(request["t"]) - int(i["start_service_time"])) < ((int(service_time) / 3) * 2) or int(i["start_service_time"]) == 0:
              json_data["playerData"]["air_cash"] = int(json_data["playerData"]["air_cash"]) - int(quick_start_coins_cost)   

                
                
            if int(json_data["planes"][j]["to_player_id"]) != 800: # ID 800 = NPC player
              print("Working")
              for file in os.listdir(os.path.join(p, "data")):
                if file[0:8] == str(json_data["planes"][j]["to_player_id"]):
                  player_to_file = file
                  break

              f = open(os.path.join(p, "data", player_to_file), "r")
              json2_data = json.loads(str(f.read()))
              f.close()
              
              last_id = int(json2_data["playerData"]["next_object_id"])
              json2_data["planes"].append(json_data["planes"][j].copy())
              json2_data["planes"][len(json2_data["planes"]) - 1]["id"] = last_id + 1
              json2_data["planes"][len(json2_data["planes"]) - 1]["buddy_points"] = buddy_points
              
              json2_data["playerData"]["next_object_id"] = int(json2_data["playerData"]["next_object_id"]) + 1

            rpcResult["r"]["planes"][str(request["p"]["id"])] = json_data["planes"][j]
        j = j + 1


    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
    
    if player_to_file != 0:
      f = open(os.path.join(p, "data", player_to_file), "w")
      f.write(json.dumps(json2_data))
      f.close()