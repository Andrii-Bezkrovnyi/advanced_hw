"""
Task 2-3:
UDP client that sends two numbers to a UDP server and prints the response.
"""
import socket


def send_numbers(a, b, host="127.0.0.1", port=8000):
    """Send two numbers to the UDP server and print the response."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = f"{a},{b}"
    sock.sendto(message.encode("utf-8"), (host, port))

    data, _ = sock.recvfrom(1024)
    print("Server response:", data.decode("utf-8"))
    sock.close()


if __name__ == "__main__":
    # Example usage
    send_numbers(12, 34)
    send_numbers(5.5, 7.3)
    send_numbers("abc", 10)  # example of invalid input
