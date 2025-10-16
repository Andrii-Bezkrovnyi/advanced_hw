"""
Task 2-7:
A simple chat server using selectors for handling multiple clients.
"""
import selectors
import socket
import threading

sel = selectors.DefaultSelector()


def input_thread(sock):
    """Thread to handle user input and send to server"""
    try:
        while True:
            msg = input()
            if msg.strip():
                sock.send(msg.encode())
    except Exception:
        pass


def start_client(host="127.0.0.1", port=8000):
    """Start the chat client"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.setblocking(False)

    sel.register(sock, selectors.EVENT_READ, data="server")

    print("Connected to chat. Type messages and press Enter (Ctrl+C to exit).")

    # Start input thread
    threading.Thread(target=input_thread, args=(sock,), daemon=True).start()

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data == "server":
                    data = sock.recv(1024)
                    if data:
                        print("\n" + data.decode())
                    else:
                        print("Server closed connection")
                        return
    except KeyboardInterrupt:
        print("Disconnected from chat")
    finally:
        sel.unregister(sock)
        sel.close()
        sock.close()


if __name__ == "__main__":
    start_client()
