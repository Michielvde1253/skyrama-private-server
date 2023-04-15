import time
from pathlib import Path
import os
import json

def handle_flashcookiesSet(request, user_id, rpcResult, items_to_add_to_obj):

    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = None