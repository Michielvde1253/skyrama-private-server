import time
from pathlib import Path
import os
import json
import userManager

def handle_planesSendback(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None
    items_to_add_to_obj.append(f"planes:{request["p"]["id"]}")

    p = Path(__file__).parents[1]     
    
    j = 0
    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
            plane_type_id = int(i["plane_type_id"])
            if request["p"]["player_id"] == 0: # Cashcow, so make it appear on radar again.
                json_data["planes"][j]["flight_status"] = 122
                json_data["planes"][j]["start_service_time"] = 0
                json_data["planes"][j]["last_state_change_time"] = request["p"]["last_state_change_time"]
                json_data["planes"][j]["player_id"] = request["p"]["player_id"]
                json_data["planes"][j]["subcontainer_id"] = request["p"]["subcontainer_id"]
                json_data["planes"][j]["container_id"] = request["p"]["container_id"]
                json_data["planes"][j]["to_player_id"] = request["p"]["to_player_id"]
                json_data["planes"][j]["instantland"] = request["p"]["instantland"]
            else:
                for g in init_data["planeTypes"]:
                  if int(g["id"]) == plane_type_id:
                    buddy_points = int(g["buddy_points_yield"])
                    break
                  
                '''
                for file in os.listdir(os.path.join(p, "data")):
                    if file[0:8] == str(json_data["planes"][j]["player_id"]):
                        player_from_file = file
                        break
                f = open(os.path.join(p, "data", player_from_file), "r")
                json2_data = json.loads(str(f.read()))
                f.close()
                '''
                json2_data = userManager.load_save_by_id(json_data["planes"][j]["player_id"])
                
                for g in json2_data["planes"]:
                  if int(g["id"]) == int(i["fromUser_objectId"]):
                    g["buddy_points"] = buddy_points
                    break

                json_data["planes"].pop(j)
            
        j = j + 1
    
    if request["p"]["player_id"] != 0:
      '''
      f = open(os.path.join(p, "data", player_from_file), "w")
      f.write(json.dumps(json2_data))
      f.close()
      '''
      userManager.modify_save_by_id(json2_data["playerData"]["account_id"], json2_data)
