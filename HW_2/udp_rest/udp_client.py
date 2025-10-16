"""Task 2-2: UDP Client that sends a unique device ID to a server."""
import socket
import uuid


def send_device_id(host="127.0.0.1", port=8000):
    """Send a unique device ID to the specified UDP server."""
    # Generate a unique device ID
    device_id = str(uuid.uuid4())

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(device_id.encode("utf-8"), (host, port))

    print(f"Device with ID {device_id} sent presence message to {host}:{port}")


if __name__ == "__main__":
    send_device_id()
