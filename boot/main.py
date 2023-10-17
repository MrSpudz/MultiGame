# init
from cpuinfo import get_cpu_info
from platform import architecture, node, platform
from os import path, system
from datetime import datetime


def clear():
    system('clear')


# Log Relative Path Setup
absolutePath = path.dirname(__file__)
logRelPath = "/logs"
logFullPath = path.join(absolutePath, logRelPath)

# Main Relative Path Setup
absolutePath = path.dirname(__file__)
relPath = "../main/"
fullPath = path.join(absolutePath, relPath)

my_cpuinfo = get_cpu_info()

f = open(path.dirname(__file__) + '/../logs/game.log', 'w').close

f = open(path.dirname(__file__) + '/../logs/game.log', 'a')
f.write("Log file created at " + str(datetime.now()) + "\n")
f.write(f"Architecture: {architecture()}\n")
f.write(f"Computer Name: {node()}\n")
f.write(f"Operating system: {platform()}\n")
f.write(f"Processor: " + str(my_cpuinfo['brand_raw']) + "\n")
f.write("Random games made by MrSpudz\n")
f.close()

with open(fullPath + "start.py") as f:  # Opens the Menu Page
    exec(f.read())

quit()
