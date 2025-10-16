"""
Task 2-7:
A simple chat server using selectors for handling multiple clients.
"""
import selectors
import socket

sel = selectors.DefaultSelector()
clients = {}  # sock -> nickname


def accept_wrapper(sock):
    """Accept new client connection"""
    conn, addr = sock.accept()
    print(f"[NEW CONNECTION] {addr}")
    conn.setblocking(False)
    # send prompt for nickname
    conn.send(b"Enter your nickname: ")
    sel.register(conn, selectors.EVENT_READ, data=addr)
    clients[conn] = None  # nickname will be set later


def broadcast(sender_sock, message: bytes):
    """Send message to all clients except sender"""
    for sock, nick in clients.items():
        if sock != sender_sock and nick:
            try:
                sock.send(message)
            except Exception:
                pass


def service_connection(key, mask):
    """Handle client messages"""
    sock = key.fileobj
    addr = key.data
    if mask & selectors.EVENT_READ:
        try:
            data = sock.recv(1024)
        except ConnectionResetError:
            data = None
        if data:
            msg = data.decode().strip()
            if clients[sock] is None:
                # first message = nickname
                nickname = msg
                clients[sock] = nickname
                sock.send(f"Welcome, {nickname}! Start chatting...\n".encode())
                print(f"[NICKNAME] {addr} is now known as {nickname}")
                broadcast(
                    sock,
                    f"[SERVER] {nickname} has joined the chat.\n".encode()
                )
            else:
                nickname = clients[sock]
                full_msg = f"[{nickname}] {msg}".encode()
                print(full_msg.decode())
                broadcast(sock, full_msg)
        else:
            nickname = clients.get(sock) or str(addr)
            print(f"[DISCONNECTED] {nickname}")
            sel.unregister(sock)
            sock.close()
            if sock in clients:
                del clients[sock]
                broadcast(
                    sock,
                    f"[SERVER] {nickname} has left the chat.\n".encode()
                )


def run_server(host="127.0.0.1", port=8000):
    """Run the chat server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    server.setblocking(False)
    sel.register(server, selectors.EVENT_READ, data=None)
    print(f"Server started on {host}:{port} ...")

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("Server stopped")
    finally:
        sel.close()


if __name__ == "__main__":
    run_server()
