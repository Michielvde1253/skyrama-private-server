import time

def handle_playerdataUpdateLevel(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None

    # Handling this in server.py instead, as for some reason the game doesn't always send this command???
    # Or is that only on the first 2 levels???
