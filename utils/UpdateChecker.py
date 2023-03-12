import requests
import webbrowser
from colorama import Fore

def check_for_update(version):
    newest = requests.get("https://raw.githubusercontent.com/gokiimax/Smaug-Reverse-Shell/main/version.txt").content.decode('utf-8')
    if newest == version:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Smaug is up to date!")
    else:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}] {Fore.RED}There is a new update available! {newest}")
        webbrowser.open("https://github.com/gokiimax/Smaug-Reverse-Shell")