import asyncio
import websockets
import flight
import json
async def connect_websocket():
    uri = "ws://3.139.94.118:3000"  # Replace with your WebSocket server URL

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        while True:
            # Send location data to the server
            if flight.home:
                print(flight.home,12321)
                await websocket.send(json.dumps({"latitude":flight.home.lat,
                                                 "longtitude":flight.home.lon,
                                                 "altitude":flight.home.alt}))


            # Wait for incoming message from the server
            response = await websocket.recv()
            response=json.loads(response)
            print(f"Received: {response}")
            flight.mission(response)


asyncio.get_event_loop().run_until_complete(connect_websocket())
