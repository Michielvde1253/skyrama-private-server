print (" [+] Loading basics...")
import os
import json
from pathlib import Path
import uuid
import time
import random
import re
if os.name == 'nt':
    os.system("color")

os.system("title Skyrama Server")

print (" [+] Loading server...")
from flask import Flask, render_template, send_from_directory, request, redirect, session, url_for
from flask.debughelpers import attach_enctype_error_multidict
from bundle import ASSETS_DIR, TEMPLATES_DIR, STUB_DIR, STYLES_DIR
from commands import *

for module in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module


available_commands = {
    "general.getCv": handle_getCv,
    "general.soundIsOn": handle_soundIsOn,
    "general.getConfig": handle_getConfig,
    "general.getInitState": handle_getInitState,
    "playerdata.setbooster": handle_setbooster,
    "playerdata.setLocation": handle_setLocation,
    "buddy.getAll": handle_buddyGetAll,
    "planes.get": handle_planesGet,
    "planes.setState": handle_planesSetState,
    "placeable.place": handle_placeablePlace,
    "planes.takeMeans": handle_planesTakeMeans,
    "planes.sendback": handle_planesSendback,
    "planes.buy": handle_planesBuy,
    "account.getLatest": handle_accountGetLatest,
    "planes.send": handle_planesSend,
    "terminals.buy": handle_terminalsBuy,
    "landside_buildings.harvest": handle_landside_buildingsHarvest,
    "flashCookies.set": handle_flashcookiesSet
}

host = '0.0.0.0'
port = 5050

app = Flask(__name__, template_folder=TEMPLATES_DIR)

print (" [+] Configuring server routes...")

##########
# ROUTES #
##########

@app.route("/play")
def play():
    return render_template("play_vercel.html", userid = request.args['userid'], SERVERIP=host)

@app.route('/')
def homepage():
    return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        for i in os.listdir("data"):
            if i[8:len(i)-5] == username:
                f = open(os.path.join("data", i), "r")
                json_data = json.loads(str(f.read()))
                if json_data["playerData"]["password"] == password:
                    msg = 'Logged in successfully!'
                    return redirect(url_for('play', userid=json_data["playerData"]["account_id"]))
                else:
                    msg = 'Wrong password/username entered.'
                    return render_template('login.html', msg=msg)
        msg = 'Wrong password/username entered.'
        return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username may only contain characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill in everything.'
        else:
            uid = random.randint(10000000, 99999999)
            n = open(os.path.join("data", "new_player.json"), "r")
            json_data = json.loads(str(n.read()))
            f = open(os.path.join("data", str(uid) + str(username) + ".json"), "w+")
            json_data["playerData"]["account_id"] = uid
            json_data["playerData"]["user_name"] = username
            json_data["playerData"]["password"] = password


            # Change user-id everywhere [WHY :-( ]
            json_data["goals"]["player_id"] = uid
            json_data["backgrounds"][0]["player_id"] = uid
            json_data["planes"][0]["to_player_id"] = uid
            json_data["runways"][0]["player_id"] = uid
            json_data["hangars"][0]["player_id"] = uid
            j = 0
            for i in json_data["landsideBuildings"]:
                json_data["landsideBuildings"][j]["player_id"] = uid
                j = j + 1
            json_data["accountData"]["id"] = uid
            json_data["accountData"]["user_name"] = username

            json_data["expeditionstatus"]["player_id"] = uid
    
            f.write(json.dumps(json_data))
            f.close()
    

            msg = 'Successfully registered!'
            name = username
            return redirect(url_for('play', userid=str(uid)))

    elif request.method == 'POST':
        msg = 'Please fill in everything.'
    return render_template('registration.html', msg=msg)

@app.route("/crossdomain.xml")
def crossdomain():
    return send_from_directory(STUB_DIR, "crossdomain.xml")

## GAME STATIC


@app.route("/assets/<path:path>")
def static_assets_loader(path):
    return send_from_directory(ASSETS_DIR, path)

@app.route("/templates/styles/<path:path>")
def styles(path):
    return send_from_directory(STYLES_DIR, path)

################
# GAME DYNAMIC #
################


@app.route("/SkyApi.php", methods=['POST'])
def handle_request():
    print(request.form)
    command_data = json.loads(request.form["d"])
    total_response = {"rpcResults":[]}
    for command in command_data:
        if command["m"] in available_commands:
            print("Command " + command["m"] + " handled")

            # Create command answer
            rpcResult = {}
            handler = available_commands[command["m"]]
            handler(command, request.form["userId"], rpcResult)

            total_response["rpcResults"].append(rpcResult)

            # Check goal completion
            handle_goal(command, request.form["userId"])

            # Create command object
            obj = {}
            handle_addObj(command, request.form["userId"], obj)

            total_response["obj"] = obj
        else:
            print("Command " + command["m"] + " not handled")
    return total_response


########
# MAIN #
########

print (" [+] Running server...")

if __name__ == '__main__':
    app.secret_key = 'SECRET_KEY'
    app.run(host=host, port=port, debug=True)
