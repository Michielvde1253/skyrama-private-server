import time
import userManager

def handle_getInitState(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    items_to_add_to_obj.append("consumablesTypes")
    items_to_add_to_obj.append("consumables")
    items_to_add_to_obj.append("packagesTypes")
    items_to_add_to_obj.append("planeUpgrades")
    items_to_add_to_obj.append("planeUpgradeTypes")
    items_to_add_to_obj.append("planeUpgradeCostTypes")

    # Store session time
    json_data["playerData"]["session_start_time"] = int(time.time())

    # Make CashCow appear on the radar
    if request["t"] > int(json_data["planes"][0]["arrival_time"]):
        # To-do: Restart tutorial if not completed.
        for i in json_data["planes"]:
            if int(i["id"]) == 0:
                i["departure_time"] = request["t"] - 450
                i["arrival_time"] = request["t"] + 450
                i["flight_status"] = 77 # in air
                break

    # Run buddy.getAll
    for buddy in json_data["buddyStuff"]["buddies"]:
        buddy_data = userManager.load_save_by_id(buddy["hi_player_id"])
        buddy["last_buddyping_time"] = buddy_data["playerData"]["last_buddyping_time"]
        buddy["xp"] = buddy_data["playerData"]["xp"]
        # if request accepted
        if int(buddy["status"]) != 1 and int(buddy["status"]) != 2:
            # if buddyping activated
            if request["t"] < int(buddy["last_buddyping_time"]):
                buddy["status"] = 5
            else:
                buddy["status"] = 0

    rpcResult["r"] = {**json_data, **init_data} # Merge both global init and personal user init.
    