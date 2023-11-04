import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        # Process the received message, e.g., echo it back to the client
        await websocket.send(f"server: {message}")

start_server = websockets.serve(handle_connection, "192.168.0.8", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
