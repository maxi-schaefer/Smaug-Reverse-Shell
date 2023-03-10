import time
from utils.config import *
from pypresence import Presence

class Discord():

    def __init__(self, client_id):
        RPC = Presence(client_id)
        RPC.connect()
        RPC.update(
            state="Time is what determines security",
            large_image="large",
            large_text="Smaug",
            small_image="small",
            small_text="Reverse Shell",
            buttons=[{"label": "Check It out!", "url": "https://github.com/gokiimax/Smaug"}],
            start=time.time()
        )