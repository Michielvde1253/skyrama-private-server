def handle_SellProducts(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "planes.takeMeans":
        if "products_sold" in request["p"]:
            if int(task["obj_type_id"]) == int(request["p"]["types_id"]) or int(task["obj_type_id"]) == -1:
                json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] += request["p"]["products_sold"]
    
    return json_data
