import socket
HOST = '192.0.2.20'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Informe sua mensagem: \n'
msg = raw_input()
while msg <> '\x18':
    udp.sendto (msg, dest)
    msg = raw_input()
udp.close()