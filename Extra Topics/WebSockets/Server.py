import asyncio  # Importing the Libraries
import websockets

""" 
    defining Callback function for WebSocket server
    THIS will communicate with the connected clients.
    which receives message from client and sends the response & handle the case 
    when any client closes the connection gracefully 
"""


async def my_accept(websocket, path):
    """ using this try and except blocks to catch exception, and specify 'connectionless' which is raised when
                 the client close connection, it will print this message"""
    try:
        while True:
            data_receive = await websocket.recv()
            if not data_receive:
                break  # Client has closed the connection
            print("Received data from client: " + data_receive)
            await websocket.send("WebSocket server sends: " + data_receive)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed gracefully")


# Creating a WebSocket server
websocket_server = websockets.serve(my_accept, "localhost", 3000)
print(" --> WebSocket Server: Waiting for client connections")

""" Create a WebSocket server using websockets.serve. 
    It shows on localhost at port 3000.
"""

# Starting the event loop to listen for incoming connections
asyncio.get_event_loop().run_until_complete(websocket_server)  # using this event_loop to run the websockets Server
asyncio.get_event_loop().run_forever()

how garbage collector works in pythoon, memory reallocate kai rite thay che
iv kai memory ma allocate che ae dekhade
what is shalow copy anc deep copy (object oriented ni ander use thayu)
python through direct open ai ne connect krvu hoi to koi kai api use karvanu
