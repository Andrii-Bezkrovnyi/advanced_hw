"""
Task 6-2:
Simple asynchronous client for testing the asyncio socket server.
"""

import asyncio


async def tcp_client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    print("🟢 Connected to server. Type messages (type 'exit' to quit):")
    while True:
        message = input("> ")
        if message.lower() == "exit":
            print("👋 Closing connection.")
            break

        writer.write((message + "\n").encode())
        await writer.drain()

        data = await reader.readline()
        print(f"💬 Server replied: {data.decode().strip()}")

    writer.close()
    await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(tcp_client())
