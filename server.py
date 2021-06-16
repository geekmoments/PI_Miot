import socket
import sys

# Crear socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind del socket a un puerto
server_address = ('', 10000)
print >>sys.stderr, 'arrancando en el puerto %s ip %s' % server_address
sock.bind(server_address)

# Escuchar conexiones entrantes
sock.listen(5)

while True:
    # Esperar una conexion
    print >>sys.stderr, 'Esperando una conexion'
    connection, client_address = sock.accept()
	
    try:
        print >>sys.stderr, 'conexion desde ', client_address

        # Recibe los datos de a pedazos y los muestra
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'recibido "%s"' % data
            if data:
                if data[0] == 'p':
                    print >>sys.stderr, 'prendo LED'
                if data[0] == 'a':
                    print >>sys.stderr, 'apago LED'
            else:
                print >>sys.stderr, 'No mas datos de ', client_address
                break
            
    finally:
        # Limpiar la conexion
        connection.close()	

