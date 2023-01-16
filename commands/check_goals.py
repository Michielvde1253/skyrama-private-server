import time
from pathlib import Path
import os
import json
from commands.goals import *

available_task_types = {
    "LandPlane": handle_LandPlane,
    "PlaceBay": handle_PlaceBay,
    "ReturnPlane": handle_ReturnPlane,
    "BuyPlane": handle_BuyPlane,
    "SendPlane": handle_SendPlane,
    "QuickStartPlane": handle_QuickStartPlane,
    "PlaceTerminal": handle_PlaceTerminal,
    "GetPassengers": handle_GetPassengers
}


def handle_goal(request, user_id):
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

    current_main_goal = json_data["goals"]["goals"]["main"]
    num_tasks_completed = 0

    i = 0
    for task in current_main_goal["tasks"]:
        print(task["user_action"])
        if task["user_action"] in available_task_types:
            handler = available_task_types[task["user_action"]]
            json_data = handler(request, user_id, json_data, task, i)

            if json_data["goals"]["goals"]["main"]["tasks"][i]["num_completed"] >= json_data["goals"]["goals"]["main"]["tasks"][i]["num_required"]:
                num_tasks_completed = num_tasks_completed + 1
        i = i + 1
        
    if num_tasks_completed == len(json_data["goals"]["goals"]["main"]["tasks"]):
        # QUEST COMPLETED, GIVE REWARDS AND START NEW QUEST
        g = 0
        for j in init_data["goalTypes"]:
            if int(j["id"]) == int(json_data["goals"]["goals"]["main"]["goal_types_id"]):
                new_goal_id = init_data["goalTypes"][g + 1]["id"]
                new_goal_i = g + 1

                json_data["playerData"]["air_coins"] = json_data["playerData"]["air_coins"] + init_data["goalTypes"][g]["reward_air_coins"]
                json_data["playerData"]["air_cash"] = json_data["playerData"]["air_cash"] + init_data["goalTypes"][g]["reward_air_cash"]
                json_data["playerData"]["xp"] = json_data["playerData"]["xp"] + init_data["goalTypes"][g]["reward_xp"]
                # To-do: other rewards
                break
            g = g + 1
        g = 0
        new_tasks = []
        for j in init_data["taskTypes"]:
            if int(j["goal_types_id"]) == int(new_goal_id):
                new_task = j
                new_task["num_completed"] = 0
                new_tasks.append(new_task)
            g = g + 1
        json_data["goals"]["goals"]["main"] = {}
        json_data["goals"]["goals"]["main"]["goal_types_id"] = new_goal_id
        json_data["goals"]["goals"]["main"]["seq_num"] = init_data["goalTypes"][new_goal_i]["seq_num"]
        json_data["goals"]["goals"]["main"]["tasks"] = []
        json_data["goals"]["goals"]["main"]["tasks"] = new_tasks


    f = open(os.path.join(p, "data", player_file), "w")
    f.write(json.dumps(json_data))
    f.close()

