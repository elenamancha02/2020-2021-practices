from Client import Client

IP = "127.0.0.1"
PORT = 8080

print("-----| Practice 3, Exercise 7 |------")

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
answer = c.talk("PING")
print(answer)

print("* Testing GET...")
seq = c.talk("GET 0")
print(f"GET 0: {seq}")
answer = c.talk("GET 1")
print(f"GET 1: {answer}")
answer = c.talk("GET 2")
print(f"GET 2: {answer}")
answer = c.talk("GET 3")
print(f"GET 3: {answer}")
answer = c.talk("GET 4")
print(f"GET 4: {answer}")

print("* Testing INFO...")
response = c.talk(f"INFO {seq}")
print(response)

print("* Testing COMP...")
print(f"COMP {seq}")
response = c.talk(f"COMP {seq}")
print(response)

print("* Testing REV...")
print(f"REV {seq}")
response = c.talk(f"REV {seq}")
print(response)

print("* Testing GENE...")
print("GENE U5")
response = c.talk("GENE U5")
print(response)


print("GENE ADA")
response = c.talk("GENE ADA")
print(response)

print("GENE FRAT1")
response = c.talk("GENE FRAT1")
print(response)

print("GENE FXN")
response = c.talk("GENE FXN")
print(response)


print("GENE RNU6_269P")
response = c.talk("GENE RNU6_269P")
print(response)

