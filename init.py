import fileinput
import os

team_name = input("Team name: ")
team_num = input("Team number:")

for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        with fileinput.FileInput(os.path.join(root, name), inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace("~~TEAM NAME~~", team_name), end='')
                print(line.replace("~~TEAM NUMBER~~", team_num), end='')