"""Task 2-2: UDP server to track connected devices by their IDs."""
import socket


def run_udp_server(host="127.0.0.1", port=8000):
    """Run a UDP server that listens for device IDs and tracks connected devices."""
    devices = set()  # to store connected device IDs

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"UDP server is listening on {host}:{port}...")

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # receive up to 1024 bytes
            device_id = data.decode("utf-8")

            if device_id not in devices:
                devices.add(device_id)
                print(f"[NEW DEVICE] ID: {device_id} from {addr}")
            else:
                print(f"[KNOWN DEVICE] ID: {device_id} from {addr}")

    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    finally:
        sock.close()
        print("Socket closed!")


if __name__ == "__main__":
    run_udp_server()
