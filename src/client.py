import asyncio
import websockets

async def connect():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to server")
        await websocket.send("Hello Server!")
        print("client still connected")
        response = await websocket.recv()
        print("still connected")
        print(f"Receivef: {response}")
        
asyncio.run(connect())