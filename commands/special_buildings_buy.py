import time

def handle_specialBuildingsBuy(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None

    for i in init_data["specialBuildingTypes"]:
      if int(i["id"]) == int(request["p"]["types_id"]):
        json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] - i["air_coins_cost"]
        json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - i["air_cash_cost"]
        json_data["playerData"]["event_currency"] = json_data["playerData"]["event_currency"] - i["event_currency_cost"]
            
        json_data["specialBuildings"].append({"sbId":"1","special_building_types_id":request["p"]["types_id"],"id":json_data["playerData"]["next_object_id"],"position_x":request["p"]["position_x"],"position_y":request["p"]["position_y"],"direction":request["p"]["direction"],"player_id":user_id})
        # What is sbId??? Doesn't seem to matter for now
    
        json_data["playerData"]["next_object_id"] = int(json_data["playerData"]["next_object_id"]) + 1