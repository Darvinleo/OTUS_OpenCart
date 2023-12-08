import socket

def get_host_ip():
    try:
        # Create a temporary socket to retrieve the IP address
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        host_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return host_ip
    except socket.error:
        return None