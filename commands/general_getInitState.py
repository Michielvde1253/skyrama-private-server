import time

def handle_getInitState(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    items_to_add_to_obj.append("consumablesTypes")
    items_to_add_to_obj.append("consumables")
    items_to_add_to_obj.append("packagesTypes")
    items_to_add_to_obj.append("planeUpgrades")
    items_to_add_to_obj.append("planeUpgradeTypes")
    items_to_add_to_obj.append("planeUpgradeCostTypes")

    json_data["playerData"]["session_start_time"] = int(time.time())

    if True: # NEW PLAYER, SET UP CASHCOW           TO BE FIXED!
        # To-do: Restart tutorial if not completed.
        json_data["planes"][0]["departure_time"] = int(time.time()) - 450
        json_data["planes"][0]["arrival_time"] = int(time.time()) + 450 

    rpcResult["r"] = {**json_data, **init_data} # Merge both global init and personal user init.
    