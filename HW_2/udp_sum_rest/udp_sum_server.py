"""
Task 2-3:
UDP server that receives two numbers, computes their sum, and sends back the result.
"""
import socket


def run_udp_server(host="127.0.0.1", port=8000):
    """Run a UDP server that sums two numbers sent by clients."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"UDP server listening on {host}:{port}...")

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # receive up to 1024 bytes
            message = data.decode("utf-8").strip()

            try:
                a_str, b_str = message.split(",")
                a, b = float(a_str), float(b_str)
                result = a + b
                response = f"Sum: {result}"
            except Exception as e:
                response = f"Error: invalid input. {e}"

            sock.sendto(response.encode("utf-8"), addr)
            print(f"Received '{message}' from {addr}, sent '{response}'")

    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    finally:
        sock.close()
        print("Socket closed. Goodbye!")


if __name__ == "__main__":
    run_udp_server()
