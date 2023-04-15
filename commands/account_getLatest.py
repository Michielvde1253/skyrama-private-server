import time
from pathlib import Path
import os
import json

def handle_accountGetLatest(request, user_id, rpcResult, items_to_add_to_obj):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = []

    rpcResult["r"].append({"username":"NPC","player_id":"800","last_ping_time":1636017485})