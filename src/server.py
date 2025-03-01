import asyncio
import websockets

async def handler(websocket):
    # print(f"New connection from path: {path}") 
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")
        
async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server is running and waiting for connections...") 
        await asyncio.Future()
        
asyncio.run(main())
        
        