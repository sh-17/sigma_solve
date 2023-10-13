""" Inside this Code I m Creating an websockets server and client that can communicate
    with each other. sever will handles disconnections, and the client sends messages to the server
    while receiving responses"""

import asyncio
import websockets

""" Function to connect to the WebSocket server:  Inside the my_connect function, I use async to create and manage a WebSocket connection.
        We send a message to the server and then receive a response."""
async def my_connect():
    """ my_connect function which establish a connection to the websocket server as 'ws://localhost:3000'. """
    async with websockets.connect("ws://localhost:3000") as websocket:

        for i in range(1, 5):
            await websocket.send("Hi Server, I'm Client")
            data_recv = await websocket.recv()
            print("Data received from server: " + data_recv)


# Connect to the WebSocket server
asyncio.get_event_loop().run_until_complete(my_connect())  # using this event loop to run my_connect function

