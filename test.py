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
            if flight.vehicle.location.global_relative_frame:
                await websocket.send(json.dumps({"latitude":flight.vehicle.location.global_relative_frame.lat,
                                                 "longitude":flight.vehicle.location.global_relative_frame.lon,
                                                 "altitude":flight.vehicle.location.global_relative_frame.alt}))
                await asyncio.sleep(1)


            # Wait for incoming message from the server
            response = await websocket.recv()
            response=json.loads(response)
            print(f"Received: {response}")
            flight.mission(response)

asyncio.run(connect_websocket())
