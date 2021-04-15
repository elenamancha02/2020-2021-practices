
def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip=False)
    print("To server:", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n","").replace("\r","")
def ping(cs):
    print_colored("PING commmand", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())