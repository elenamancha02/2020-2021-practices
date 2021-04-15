import termcolor
import socket
from seq import Seq

list_sequences = ["AGCTTTTGAAACCCCG", "TGAACTGAAACGT", "GACGTACGACCCAGT", "AGAGCTATGAAAGGGCC", "TAGGGGTTCCCGATAGC"]
PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
count_connections = 0
ls.listen()

termcolor.cprint("The server is configured!", 'white')
client_adress_list = []
while True:
    termcolor.cprint("Waiting for Clients to connect", 'white')

    try:
        (cs, client_ip_port) = ls.accept()
        client_adress_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION" + str(count_connections)+ ". CLIENT IP, PORT: "+ str(client_ip_port))
    except KeyboardInterrupt:
        termcolor.cprint("Server stopped by the user",'white')
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        if msg == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!\n"
            termcolor.cprint(f"{response}", 'white')
            cs.send(response.encode())
            cs.close()

        elif msg.startswith("GET"):
            parts = msg.split(" ")
            try:
                number = int(parts[1])
                if 0 <= number <= len(list_sequences):
                    termcolor.cprint("GET", 'green')
                    seq = list_sequences[number]
                    termcolor.cprint(f"{seq}\n", 'white')
                    cs.send(f"{seq}".encode())
                    cs.close()
            except ValueError:
                pass

        elif msg.startswith("INFO"):
            parts = msg.split(" ")
            if len(parts) == 2 and parts[0] == "INFO":
                termcolor.cprint("INFO", 'green')
                seq = Seq(parts[1])
                info = seq.info()
                termcolor.cprint(f"{info}", 'white')
                cs.send(f"{info}".encode())
                cs.close()

        elif msg.startswith("COMP"):
            parts = msg.split(" ")
            if len(parts) == 2 and parts[0] == "COMP":
                termcolor.cprint("COMP", 'green')
                seq = Seq(parts[1])
                complem = seq.complement()
                termcolor.cprint(f"{complem}\n", 'white')
                cs.send(f"{complem}\n".encode())
                cs.close()

        elif msg.startswith("REV"):
            parts = msg.split(" ")
            if len(parts) == 2 and parts[0] == "REV":
                termcolor.cprint("REV", 'green')
                seq = Seq(parts[1])
                rev = seq.reverse()
                termcolor.cprint(f"{rev}\n", 'white')
                cs.send(f"{rev}\n".encode())
                cs.close()

        elif msg.startswith("GENE"):
            parts = msg.split(" ")
            if len(parts) == 2 and parts[0] == "GENE":
                termcolor.cprint("GENE", 'green')
                filename = f"{parts[1]}.txt"
                seq = Seq()
                seq.read_fasta(filename)
                termcolor.cprint(f"{seq}\n", 'white')
                cs.send(f"{seq}\n".encode())
                cs.close()

