import time
from pathlib import Path
import os
import json

def handle_terminalsBuy(request, user_id, rpcResult):
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

    terminal = {}
    terminal["terminal_types_id"] = request["p"]["types_id"]
    terminal["last_harvest_time"] = request["p"]["last_harvest_time"]
    terminal["set_in_storage_time"] = request["p"]["set_in_storage_time"]
    terminal["id"] = request["p"]["id"]
    terminal["position_x"] = request["p"]["position_x"]
    terminal["position_y"] = request["p"]["position_y"]
    terminal["direction"] = request["p"]["direction"]
    terminal["player_id"] = user_id

    json_data["terminals"].append(terminal)

    json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - request["p"]["influenceableType"]["air_coins_cost"]
    json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - request["p"]["influenceableType"]["air_cash_cost"]
    json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - request["p"]["influenceableType"]["event_currency_cost"]

    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()
