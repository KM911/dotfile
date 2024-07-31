#!/usr/bin/env python3
# get all the folders , and


# every time I have to dedice the which path

import subprocess


process = subprocess.run(['fd', '.go'], stdout=subprocess.PIPE)

text = process.stdout.decode('utf-8')


tools = text.strip().split("\n")
tools = [i for i in tools if i != "main.go"]
main_go = [
    "package main",
    "import \"toolbox/tools\"",
    "func main() {",
    "function()",
    "}",]


def build(mod: str):
    with open("main.go", "w") as file:
        # UpMod = mod.capitalize()
        UpMod = mod.split("/")
        cmd = UpMod[-1]
        UpMod[-1] = cmd.capitalize()
        main_go[3] = f"{".".join(UpMod)}()"
        file.write("\n".join(main_go))
    subprocess.run(['go', 'build', "-o", "./target/"+cmd,  '.'])
    # subprocess.run(['go', 'build', "-o", "/usr/bin/"+mod,  '.'])
    # subprocess.run(['sudo', 'mv', "./" + mod, "/usr/bin/"+mod])


mods = [i[:-3] for i in tools]

# build("hello")
for i in mods:
    build(i)
