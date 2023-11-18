def handle_FillShop(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "cargoshops.fillShop":
        if int(task["obj_type_id"]) == int(request["p"]["cargo_shop_types_id"]) or int(task["obj_type_id"]) == -1:
            json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] += request["p"]["capacity"]
    
    return json_data
