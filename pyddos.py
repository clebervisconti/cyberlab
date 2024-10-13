import socket
import concurrent.futures
import sys

# Define the IP address and ports to check
ip_address = 'your.ip.address.here'  # replace with your target IP address
ports = [80, 8080, 21, 22, 8089]

# Function to check if a port is open
def ping_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout for the connection attempt
        try:
            s.connect((ip, port))
            return f"Port {port} on {ip} is open"
        except (socket.timeout, ConnectionRefusedError):
            return f"Port {port} on {ip} is closed or not responding"

# Main function to run parallel port checks
def ping_ports_in_parallel(ip, ports):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(ping_port, ip, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results

# Run the script and print results
if __name__ == "__main__":
    results = ping_ports_in_parallel(ip_address, ports)
    for result in results:
        print(result)
