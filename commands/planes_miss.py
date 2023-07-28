import time

def handle_planesMiss(request, user_id, rpcResult, items_to_add_to_obj, json_data, init_data):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}
    rpcResult["r"]["planes"] = {}

    if request["p"]["id"] != 0:
      j = 0
      for i in json_data["planes"]:
        if int(i["id"]) == request["p"]["id"]:
          json_data["planes"].pop(j)
          break
        j = j + 1