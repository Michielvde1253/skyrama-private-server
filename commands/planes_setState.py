import time
from pathlib import Path
import os
import json

def handle_planesSetState(request, user_id, rpcResult, items_to_add_to_obj):
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

    j = 0
    for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
            json_data["planes"][j]["last_state_change_time"] = request["p"]["last_state_change_time"]
            json_data["planes"][j]["player_id"] = request["p"]["player_id"]
            json_data["planes"][j]["subcontainer_id"] = request["p"]["subcontainer_id"]
            json_data["planes"][j]["container_id"] = request["p"]["container_id"]
            json_data["planes"][j]["to_player_id"] = request["p"]["to_player_id"]
            json_data["planes"][j]["to_location_id"] = request["p"]["to_location_id"]
            json_data["planes"][j]["instantland"] = request["p"]["instantland"]
            json_data["planes"][j]["flight_status"] = request["p"]["flight_status"]
            json_data["planes"][j]["to_user_name"] = request["p"]["to_user_name"]  

            # To-do: clean up code + check ramacopters/waterplanes
            # 2 = getting out of the hangar
            # 1005 = landed, plane still on runway (own plane)
            # 105 = landed, plane still on runway (buddy plane)
            # others: don't remember
            if request["p"]["flight_status"] == 118 or request["p"]["flight_status"] == 1010 or request["p"]["flight_status"] == 9 or request["p"]["flight_status"] == 2 or request["p"]["flight_status"] == 1005 or request["p"]["flight_status"] == 105:
                json_data["planes"][j]["start_service_time"] = request["p"]["last_state_change_time"]


            # Reduce aircash if buddy plane is landed instantly

            if int(request["p"]["instantland"]) == 1:
                if request["p"]["flight_status"] == 105:

                    f = open(os.path.join(p, "data", "global_init_data.json"), "r")
                    init_data = json.loads(str(f.read()))
                    f.close()

                    for g in init_data["planeTypes"]:
                        if int(g["id"]) == int(i["plane_type_id"]):
                            air_cash_cost = int(g["quick_land_coins_cost"])
                            json_data["playerData"]["air_cash"] = int(json_data["playerData"]["air_cash"]) - air_cash_cost
                            break

            break
        j = j + 1
    


    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
