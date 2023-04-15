import time
from pathlib import Path
import os
import json

def handle_packagesBuy(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None
    items_to_add_to_obj.append("consumables")
    
    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()  
    
    f = open(os.path.join(p, "data", "global_init_data.json"), "r")
    init_data = json.loads(str(f.read()))
    f.close()
    
    air_cash_cost = int(init_data["packagesTypes"][str(request["p"]["id"])]["air_cash_cost"])
    
    # Lazy way (amount is only readable in "name"???)
    if request["p"]["id"] == 1:
      res_earn = 25
    elif request["p"]["id"] == 2:
      res_earn = 135
      
    if json_data["consumables"] == []: # New account, initialize tuning items (first item in list doesn't count???)
            json_data["consumables"] = [0,0,0,0,0,0,0]
            
    # Add tuning items to account
    j = 0
    for i in json_data["consumables"]:
      if j != 0:
        json_data["consumables"][j] = json_data["consumables"][j] + res_earn
      j = j + 1
        
    json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] - air_cash_cost
    
    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()