import time
from pathlib import Path
import os
import json

def handle_lucky_luggage_live(request, user_id):
    p = Path(__file__).parents[1]
    for file in os.listdir(os.path.join(p, "data")):
        if file[0:8] == str(user_id):
            player_file = file
            break

    f = open(os.path.join(p, "data", player_file), "r")
    json_data = json.loads(str(f.read()))
    f.close()
    
    if "next_reward" not in json_data["lucky_luggage_data"]:
       json_data["lucky_luggage_data"]["next_reward"] = 0

    if json_data["lucky_luggage_data"]["next_reward"] < int(time.time()):
      if (json_data["lucky_luggage_data"]["next_reward"] + 86400) < int(time.time()): # If previous spin is not claimed, reset back to 1
        json_data["lucky_luggage_data"]["consecutive_login_days"] = 1
        json_data["playerData"]["consecutive_logins_begin"] = int(time.time())
        json_data["playerData"]["num_consecutive_login_days"] = 1 # Why does this always have to been on so many different places :((
      else:
        json_data["lucky_luggage_data"]["consecutive_login_days"] = json_data["lucky_luggage_data"]["consecutive_login_days"] + 1
        json_data["playerData"]["num_consecutive_login_days"] = json_data["lucky_luggage_data"]["consecutive_login_days"]
        
      days = json_data["lucky_luggage_data"]["consecutive_login_days"]
      
      json_data["lucky_luggage_data"]["next_reward"] = int(time.time()) + 86400 # After 24 hours     
      
      if days < 5:
        num_spins = int(json_data["lucky_luggage_data"]["free_spin_table"][days - 1])
      else:
        num_spins = int(json_data["lucky_luggage_data"]["free_spin_table"][4])
        
      json_data["lucky_luggage_data"]["free_spins"] = json_data["lucky_luggage_data"]["free_spins"] + num_spins
      json_data["playerData"]["lucky_luggage_free_spins"] = json_data["lucky_luggage_data"]["free_spins"] # Is this being used by the game?
        
    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()