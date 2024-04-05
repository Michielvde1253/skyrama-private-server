from pathlib import Path
import json
import os
import time


p = Path(__file__).parents[0]


'''
When save files get loaded, store them in memory as buddy.getAll needs to loop all buddies,
which is much better performance-wise if done from memory.
'''

__saves = {}

n = open(os.path.join("data", "new_player.json"), "r")
NEW_ACCOUNT_DATA = json.loads(str(n.read()))
n.close()


def store_save_by_id(user_id):
    try:
        f = open(os.path.join(p, "data", str(user_id) + ".json"), "r")
        json_data = json.loads(str(f.read()))
        __saves[str(user_id)] = json_data
        f.close() 
        return True
    except FileNotFoundError: # Account does not exist
        return False

def load_save_by_id(user_id):
    if not str(user_id) in __saves:
        if store_save_by_id(user_id) == False:
            return -1
    return __saves[str(user_id)]

def load_save_by_name(user_name):
    user_id = get_id_from_name(user_name)
    if user_id == -1:
        return -1
    else:
        return load_save_by_id(user_id)


def modify_save_by_id(user_id, json_data):
    __saves[str(user_id)] = json_data
    f = open(os.path.join("data", str(user_id) + ".json"), "w")
    f.write(json.dumps(json_data))
    f.close()

def get_id_from_name(user_name):
    try:
        f = open(os.path.join(p, "data", "nametoid", str(user_name)), "r")
        user_id = int(f.read())
        f.close()
        return user_id
    except FileNotFoundError:
        return -1

def user_id_exists(user_id):
    return load_save_by_id(user_id) != -1

def user_name_exists(user_name):
    return load_save_by_name(user_name) != -1

def create_new_account(uid, username, password, token):
    json_data = NEW_ACCOUNT_DATA.copy()
    f = open(os.path.join("data", str(uid) + ".json"), "w+")
    json_data["playerData"]["account_id"] = uid
    json_data["playerData"]["user_name"] = username
    json_data["playerData"]["password"] = password

    #################################################################
    # Change user-id everywhere [WHY :-( ]                          #
    #################################################################
    json_data["goals"]["player_id"] = uid                           #
    json_data["backgrounds"][0]["player_id"] = uid                  #
    json_data["planes"][0]["to_player_id"] = uid                    #
    json_data["runways"][0]["player_id"] = uid                      #
    json_data["hangars"][0]["player_id"] = uid                      #
    json_data["bays"][0]["player_id"] = uid                       #
    j = 0                                                           #
    for i in json_data["landsideBuildings"]:                        #
        json_data["landsideBuildings"][j]["player_id"] = uid        #
        j = j + 1                                                   #
    json_data["accountData"]["id"] = uid                            #
    json_data["accountData"]["user_name"] = username                #
    json_data["expeditionstatus"]["player_id"] = uid                #
    json_data["playerData"]["token"] = token                        #
    #################################################################

    f.write(json.dumps(json_data))
    f.close()


    # Create a nametoid file
    f = open(os.path.join("data", "nametoid", str(username)), "w+")
    f.write(str(uid))
    f.close()