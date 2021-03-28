from Client0 import Client

from termcolor import colored, cprint


PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 10000
my_client = Client(IP, PORT)
cprint(my_client.debug_talk("Message 1---"), "blue")
cprint(my_client.debug_talk("Message 2: Testing !!!"), "blue")
