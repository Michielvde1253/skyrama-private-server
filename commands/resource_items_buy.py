import time

def handle_resourceItemsBuy(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None

    if request["p"]["name"] == "allyoucanquickservice":
        if json_data["playerData"]["air_cash"] >= 30:
            json_data["playerData"]["air_cash"] -= 30
            json_data["playerData"]["aycqs_start_time"] = request["p"]["time"] + 86400