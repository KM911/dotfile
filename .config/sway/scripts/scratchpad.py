#!/home/km/Templates/python/venv/bin/python

import subprocess
import json
# parse the command line arguments
# {"text":"2", "class":"two", "alt":"two", "tooltip":"f-2 | ~\nf-1 | ~\n"}

Resp = {
    "text": "",
    "class": "",
    "alt": "",
    "tooltip": ""
}


process = subprocess.run(
    ["swaymsg", "-r", "-t", "get_tree"], stdout=subprocess.PIPE)
text = process.stdout.decode('utf-8').strip()
exit_code = process.returncode

if exit_code == 0:
    obj = json.loads(text)
    shells = []
    for i in obj["nodes"][0]["nodes"][0]["floating_nodes"]:
        if i["app_id"].startswith("f-"):
            shells.append("</" + i["app_id"][2:] + ">")

    Resp["text"] = str(len(shells))
    Resp["class"] = str(len(shells))
    Resp["alt"] = str(len(shells))
    Resp["tooltip"] = "".join(shells)
    print(json.dumps(Resp))

else:
    print("error")
    print(exit_code)
