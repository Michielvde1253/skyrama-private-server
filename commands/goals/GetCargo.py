def handle_GetCargo(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "planes.takeMeans":
        if "cargo" in request["p"]:
            if int(task["obj_type_id"]) == int(request["p"]["cargo_types_id"]) or int(task["obj_type_id"]) == -1:
                json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] += int(request["p"]["cargo"])
    
    return json_data
