import asyncio
import websockets
import flight
import json

async def send_location(websocket):
    while True:
        # Send location data to the server
        if flight.home:
            if  flight.home.alt:
                await websocket.send(json.dumps({"lat":flight.home.lat,
                                                "lon":flight.home.lon,
                                                "alt":flight.home.alt}))
        await asyncio.sleep(1)  # sleep for 1 second

async def receive_messages(websocket):
    while True:
        # Wait for incoming message from the server
        response = await websocket.recv()
        response = json.loads(response)
        print(f"Received: {response}")
        flight.mission(response)

async def connect_websocket():
    uri = "ws://3.139.94.118:3000"  # Replace with your WebSocket server URL

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        sender = asyncio.create_task(send_location(websocket))
        receiver = asyncio.create_task(receive_messages(websocket))
        
        done, pending = await asyncio.wait(
            [sender, receiver],
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()

asyncio.run(connect_websocket())
