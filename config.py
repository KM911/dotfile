
# docker image
images = [
    "redis:alpine",
    "mysql:8.0",
]

# the

code = ["go", "rust", "docker", "nodejs",  "jdk-openjdk"]
code_tool = ["pnpm", "maven", "cmake"]
db = ["redis", "resp-app", "redis"]
font = ["ttf-fira-code"]
tool = ["docker"]
shell = ["wezterm", "nushell", "starship", "zoxide", "gitui"]
daily = ["obsidian", "google-chrome"]
work = ["feishu-bin"]

total = code + shell + daily + work


# Personal dotfile
Configs = ["sway", "waybar", "nushell", "helix", "rofi", "yazi", "foot"]
Etcs = ["/etc/environment", "~/.cargo/config.toml"]
Scripts = [
    "/usr/bin/pp",
    "/usr/bin/time",
    "/usr/bin/suck"
]


def ListToDict(x):
    Dict = {}
    for i in x:
        filename = i.split("/")[-1]
        Dict[filename] = i
    return Dict


EtcDict = ListToDict(Etcs)
ScriptsDict = ListToDict(Scripts)
