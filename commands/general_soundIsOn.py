import time
from pathlib import Path
import os
import json

def handle_soundIsOn(request, user_id, rpcResult):
    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = 1 # To-do: Make it read the save file (+ let the settings work)