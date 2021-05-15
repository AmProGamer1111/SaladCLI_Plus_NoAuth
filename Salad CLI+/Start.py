import os
import time
import requests
import sys
import pyperclip
import json
import webbrowser
from colorama import Fore, Back

os.system("cls")
sys.stdout.write("\x1b]2;Salad CLI+ | By Walkx\x07")

with open('config.json') as f:
    js = json.load(f)
with open('./Art/Login screen.txt', encoding='utf-8') as f:
    loginscreen = f.read()

print(Fore.GREEN + loginscreen)

# Input Selection
select = input(
    f"{Fore.CYAN}Select an option: {Fore.YELLOW}\n\n{Fore.YELLOW}1 - {Fore.WHITE}Start Mining \n{Fore.YELLOW}2 - {Fore.WHITE}Open Salad Store\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")
if select == "1":
    os.system('python ./Mining.py')

if select == "2":
    webbrowser.open('http://app.salad.io')

os.system('python Start.py')