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
answer = c.talk(f"INFO {seq}")
print(answer)

print("* Testing COMP...")
print(f"COMP {seq}")
answer = c.talk(f"COMP {seq}")
print(answer)

print("* Testing REV...")
print(f"REV {seq}")
answer = c.talk(f"REV {seq}")
print(answer)

print("* Testing GENE...")
print("GENE U5")
answer = c.talk("GENE U5")
print(answer)


print("GENE ADA")
answer = c.talk("GENE ADA")
print(answer)

print("GENE FRAT1")
answer = c.talk("GENE FRAT1")
print(answer)

print("GENE FXN")
answer = c.talk("GENE FXN")
print(answer)


print("GENE RNU6_269P")
answer = c.talk("GENE RNU6_269P")
print(answer)

