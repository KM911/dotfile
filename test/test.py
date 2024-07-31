from rich import print
from rich.prompt import Confirm, Prompt

options = ["选项 1", "选项 2", "选项 3"]
optionss = [1, 2, 3]

for option in options:
    print(option)
#
choice = Prompt.ask("请选择一个选项")


# print("choice ", choice)
# if choice:
print(f"你选择了: {options[int(choice)-1]}")  # 这里可以根据实际选择情况进行处理
