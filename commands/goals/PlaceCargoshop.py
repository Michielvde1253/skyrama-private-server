def handle_PlaceCargoshop(request, user_id, json_data, task, task_number, init_data, quest_seq):
    if request["m"] == "placeable.place":
        for i in json_data["cargoShops"]:
            if int(i["id"]) == int(request["p"]["obj_id"]):
                type_id = int(i["cargo_shop_types_id"])
                break
        if request["p"]["obj_type"] == "cargoshop":
            if int(task["obj_type_id"]) == type_id or int(task["obj_type_id"]) == -1:
                json_data["goals"]["goals"][quest_seq]["tasks"][task_number]["num_completed"] += 1
    
    return json_data
