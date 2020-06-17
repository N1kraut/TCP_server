import socket

serv_sock = socket.socket(socket.AF_INET,    # задаем семейство протоколов "Интернет" (INET)
                        socket.SOCK_STREAM,  # задаем тип передачи данных "потоковый"(TCP)
                        proto=0)            # выбираем протокол "по умолчанию" для TCP, т.е. IP

serv_sock.bind(('', 53210))                 # что бы привязать сразу ко всем, можно использовать '', что мы и сделаем
serv_sock.listen(10)                        # 10 - это размер очереди входящих подключений, т.н. backlog

while True:
    #Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()
