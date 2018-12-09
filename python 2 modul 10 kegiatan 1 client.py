import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 20018))
print "Mesin penjawab otomatis sudah siap"
while pesan.lower() != 'keluar':
    pesan = raw_input('Perintah: ')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Perintah: ', response
    elif pesan.lower() == 'keluar':
        respon = s.recv(1024)
        print 'Perintah: ', respon
s.close()
