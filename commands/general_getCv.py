import time
from pathlib import Path
import os
import json

def handle_getCv(request, user_id, rpcResult):

    rpcResult["i"] = request["i"]
    rpcResult["t"] = str(int(time.time()))
    rpcResult["r"] = {}

    p = Path(__file__).parents[1]
    f = open(os.path.join(p, "assets", "getCv.json"), "r")
    cvs = json.loads(str(f.read()))

    rpcResult["r"]["cvs"] = cvs