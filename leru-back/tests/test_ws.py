def test_websocket_echo(client):
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("oi")
        assert websocket.receive_text() == "oi"
