import websocket

# Replace with your WebSocket server URL
websocket_url = 'ws://127.0.0.1:8000/ws/test/'


def on_message(ws, message):
    print(f"Received: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}: {close_msg}")


def on_open(ws):
    print("WebSocket connection opened")
    # Send a test message to the WebSocket server
    ws.send("Hello, WebSocket server!")


if __name__ == "__main__":
    websocket.enableTrace(True)  # Enable trace for debugging (optional)

    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
