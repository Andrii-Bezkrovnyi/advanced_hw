"""
Task 6-2:
Asynchronous socket server using asyncio.
Handles multiple clients concurrently.
"""

import asyncio


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """Handle communication with a single client."""
    addr = writer.get_extra_info("peername")
    print(f"🟢 New connection from {addr}")

    while True:
        data = await reader.readline()
        if not data:
            print(f"🔴 Client {addr} disconnected.")
            break

        message = data.decode().strip()
        print(f"📩 Received from {addr}: {message}")

        response = f"Echo: {message}\n"
        writer.write(response.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    """Start the asyncio TCP server."""
    host = "127.0.0.1"
    port = 8888

    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"🚀 Server started on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
