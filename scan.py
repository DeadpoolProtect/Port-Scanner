import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 193, 443, 445, 465, 587, 873, 993, 995, 3306, 3389, 5631, 5900, 6379, 11211, 25565, 30120, 8080, 2022]

def scan_ports(target):
    print(f"Scanning ports on {target}...\n")
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

target = input("Entrez l'adresse IP ou le nom du site à scanner: ")

scan_ports(target)
