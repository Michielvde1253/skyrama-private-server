import time
import userManager

def handle_accountGetLatest(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = []

    # The request from the game contains "numAccounts" as well
    # To prevent abusing we hardcode it here instead (numAccounts = 30) + we don't add last_ping_time

    player_list = userManager.get_accounts_by_location_id(request["p"]["locationId"],30,user_id)

    print(player_list)

    for player in player_list:
        if player == 800:
            username = "NPC"
        else:
            json2_data = userManager.load_save_by_id(player)
            username = json2_data["playerData"]["user_name"]

        rpcResult["r"].append({"username":username,"player_id":player,"last_ping_time":0})