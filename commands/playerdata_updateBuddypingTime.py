import time

def handle_updateBuddypingTime(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None

    json_data["playerData"]["last_buddyping_time"] = request["t"] + 1800 # = 30 minutes
