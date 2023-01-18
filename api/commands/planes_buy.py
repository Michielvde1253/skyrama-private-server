import time
from pathlib import Path
import os
import json

def handle_planesBuy(request, user_id, rpcResult):
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

    json_data["planes"].append({"souvenir_types_id":-1,"active_count":1,"id":request["p"]["id"],"plane_type_id":request["p"]["typeId"],"container_id":request["p"]["container_id"],"subcontainer_id":request["p"]["subcontainer_id"],"to_player_id":-1,"departure_time":-1,"arrival_time":-1,"kerosene_boost_flag":"0","flight_status":"77","buddy_points":0,"contents_count":5,"air_coins":20,"xp":0,"wares_revenue":5,"banner_id":"-1","start_service_time":"0","last_state_change_time":"0","drop_consumable_id":"0","drop_consumable_amount":"0","instantland":0,"player_id":user_id,"from_location_id":-1,"from_user_name":"drone","upgrade_level":0})

    f = open(os.path.join(p, "data", "global_init_data.json"), "r")
    init_data = json.loads(str(f.read()))
    f.close()

    for i in init_data["planeTypes"]:
        if int(i["id"]) == int(request["p"]["typeId"]):
            json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - i["air_coins_cost"]
            json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - i["air_cash_cost"]
            json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - i["event_currency_cost"]

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
