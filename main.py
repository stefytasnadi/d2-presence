from pypresence import Presence
import time

client_id = '914571824749228052'
RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state="Project Diablo II", details="Farming Runes", large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=time.time()))  # Set the presence

while True: 
    time.sleep(15) 
