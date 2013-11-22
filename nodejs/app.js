var io = require('socket.io').listen(9999);
var querystring = require('querystring');
var http = require('http');


io.sockets.on('connection', NuevoSocket);

function NuevoSocket(socket){
	socket.on('nuevo comentario',RecibeComentario);
}

function RecibeComentario(data){
	var values = querystring.stringify(data);
	
	var options = {
		hostname: 'localhost',
		port: 8000,
		path: 'nuevo-comentario/',
		method: 'POST'
		/*headers: {
			'Content-Type': 'x-www-form-urlencoded',
			'Content-Length': values.length
		}*/
	};

	var req = http.request(options, EnviaPeticion);
		
		
	
	function EnviaPeticion(res){
		console.log("hola");
		res.setEncoding('utf8');
		res.on('data' , function(data){
			io.sockets.emit('comentario nuevo' , data);
		});
	}

	req.write(values);
	req.end();
}
