def init_events(socket):
    @socket.on("check-connection")
    async def check_connection():
        await socket.emit("confirm-connection", "confirmed")

    @socket.on("join")
    async def on_join(sid, room):
        socket.enter_room(sid, room)
        await socket.emit("joined-room", "joined", room=room)

    @socket.on("leave")
    async def on_leave(sid, room):
        socket.leave_room(sid, room)
        await socket.emit("left-room", "left", room=sid)

    @socket.on("connect")
    async def connect(sid, environ):
        print(f"Client {sid} connected")
        await socket.emit("message", {"data": "Connected"}, to=sid)

    @socket.on("disconnect")
    async def disconnect(sid):
        print(f"Client {sid} disconnected")
