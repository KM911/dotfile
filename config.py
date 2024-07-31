
# docker image
images = [
    "redis:alpine",
    "mysql:8.0",
]

# the

code = ["go", "rust"]
code_tool = []
db = ["redis", "resp-app", "mysql"]
font = ["ttf-fira-code"]

tool = ["docker", "nvtop", "inxi", "docker-buildx", "wireshark"]
shell = ["wezterm", "nushell", "starship", "zoxide", "gitui",
         "tokei", "fd", "ripgrep", "dust", "bat", "procs", "hyperfine"]
daily = ["obsidian", "google-chrome"]
work = ["feishu-bin"]

total = code + shell + daily + work + db + font + tool + code_tool


# Personal dotfile
Configs = ["sway", "waybar", "nushell",
           "helix", "rofi", "yazi", "foot", "pip", "mako", "wofi", "cava", "neofetch"]
Etcs = ["/etc/environment", "~/.cargo/config.toml", "~/.wezterm.lua"]
Scripts = [
    "/usr/bin/pp",
    "/usr/bin/time",
    "/usr/bin/bg",
    "/usr/bin/keys",
    "/usr/bin/clean-history",
    "/etc/greetd/config.toml",
]


def ListToDict(x):
    Dict = {}
    for i in x:
        filename = i.split("/")[-1]
        Dict[filename] = i
    return Dict


EtcDict = ListToDict(Etcs)
ScriptsDict = ListToDict(Scripts)


# sudo pacman -Sy fcitx5-im fcitx5-chinese-addons fcitx5-configtool

#  "registry-mirrors": [
#     "https://hub-mirror.c.163.com",
#     "https://mirror.baidubce.com"
#   ]
