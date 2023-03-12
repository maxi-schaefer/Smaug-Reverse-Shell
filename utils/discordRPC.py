import time
from utils.config import *
from pypresence import Presence

class Discord():

    def __init__(self):
        self.RPC = Presence("1083754884114956400")
        self.RPC.connect()
    
    def update(self, state, large_image, large_text, small_image, small_text, buttons, start):
        self.RPC.update(
            state=state,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text,
            buttons=buttons,
            start=start
        )