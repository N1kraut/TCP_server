import socket

serv_sock = socket.socket(socket.AF_INET,    # задаем семейство протоколов "Интернет" (INET)
                        socket.SOCK_STREAM,  # задаем тип передачи данных "потоковый"(TCP)
                        proto=0)            # выбираем протокол "по умолчанию" для TCP, т.е. IP

serv_sock.bind(('', 53210))                 # что бы привязать сразу ко всем, можно использовать '', что мы и сделаем
serv_sock.listen(10)                        # 10 - это размер очереди входящих подключений, т.н. backlog

client_sock, client_addt = serv_sock.accept()


class socket:  # Да, да, имя класса с маленькой буквы :(
      def __init__(domain, type, proto):
          self._fd = system_socket(domain, type, proto)

      def write(data):
          # на деле вместо write используется send, но об этом ниже
          system_write(self._fd, data)

      def fileno():
          return self._fd
