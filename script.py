import socket

domain = "www.kame.net"

try:
    ipv4_addrs = socket.getaddrinfo(domain, None, socket.AF_INET)
    print("IPv4 addresses:")
    for result in ipv4_addrs:
        ip = result[4][0]
        print(f" - {ip}")
except socket.gaierror:
    print("No IPv4 addresses found.")

print()

try:
    ipv6_addrs = socket.getaddrinfo(domain, None, socket.AF_INET6)
    print("IPv6 addresses:")
    for result in ipv6_addrs:
        ip = result[4][0]
        print(f" - {ip}")
except socket.gaierror:
    print("No IPv6 addresses found.")
