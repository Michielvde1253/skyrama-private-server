import time

def handle_accountGetLatest(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = []

    rpcResult["r"].append({"username":"NPC","player_id":"800","last_ping_time":1636017485})