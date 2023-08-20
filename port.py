#github.com/ranjan1560/Fast_Port_Scanner
#Developerd By Ranjan Kumar
import socket
import concurrent.futures

PORT_TO_SERVICE = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    66: "sql-net",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP",
    123: "NTP",
    137: "NetBios",
    138: "NetBios",
    139: "NetBios",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    636: "LDAPS",
    989: "FTP over TLS/SSL"
    # Add more port numbers and service names here
}

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((target, port))
            if (not result):
                service_name = PORT_TO_SERVICE.get(port, "Unknown")
                print(f"Port {port} , service:{service_name}")
    except:
        pass

def main():

    try:
        print()
        print("Enter The IP address like this-->> 8.8.8.8")
        print()
        target = input("Enter IP address for scan: ")
        start_port = int(input("Enter start port to scan: "))
        last_port = int(input("Enter last port to scan: "))
        print('Here is the lists of all open ports:')
        print()
        port_range = range(start_port, last_port+1)  # Port range to scan

        num_threads = 1000  # Number of concurrent threads

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(scan_port, target, port) for port in port_range]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)
    except Exception as e:
        print("unexpected Error !! Please decrease the num_threads ::",e)

if __name__ == "__main__":
    main()
