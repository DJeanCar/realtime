var io = require('socket.io').listen(9999);

io.sockets.on('connection' , arranque);

function arranque(socket){
	socket.on('nuevoNombre', emitir);
}

function emitir(data){
	io.sockets.emit("nombreDesdeServidor",
				data + "*");
}

	