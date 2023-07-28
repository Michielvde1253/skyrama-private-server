import time

def handle_buddyGetAll(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}

    rpcResult["r"]["buddies"] = json_data["buddyStuff"]["buddies"]
    rpcResult["r"]["packets"] = json_data["buddyStuff"]["packets"]
