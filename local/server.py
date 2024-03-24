import socket
import json


class Server:
    def __init__(self):
        host = socket.gethostname()
        port = 5000  # initiate port no above 1024
        server_socket = socket.socket()  # get instance
        server_socket.bind((host, port))  # bind host address and port together
        server_socket.listen(2)
        self.conn, self.address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(self.address))

        self.previous_VP = 0
        self.output = []

    def VP(self, PID_OUTPUT):
        # G = 2/(2s+3)
        VP = 0.7408*self.previous_VP + 0.1728 * PID_OUTPUT
        return VP

    def set_pid_parameters(self, setpoint=None, Kp=None, Ki=None, Kd=None, PID_FLAG=False):
        if PID_FLAG:
            self.setpoint = setpoint
            self.Kp = Kp
            self.Ki = Ki
            self.Kd = Kd
            parameters = {"setpoint": setpoint, "Kp": Kp,
                          "Ki": Ki, "Kd": Kd, "PID_FLAG": PID_FLAG}
        else:
            parameters = {"PID_FLAG": PID_FLAG}
        parameters = json.dumps(parameters)
        self.conn.send(parameters.encode())

    def run(self):
        print("Server started")
        while True:
            # Recebe os dados do cliente
            data = self.conn.recv(1024).decode("utf-8")

            # Se não houver dados, encerra o loop
            if not data:
                break

            print(data)
            # Converte os dados recebidos em um objeto JSON
            dado = json.loads(str(data))

            # Imprime o tipo dos dados
            print(dado)

            # Extrai o valor de 'PID_OUTPUT' dos dados
            data = dado["PID_OUTPUT"]

            # Converte 'PID_OUTPUT' em um float
            data = float(data)

            # Chama a função VP com 'data' como argumento, converte o resultado em JSON e codifica em bytes
            data = json.dumps(self.VP(data)).encode("utf-8")

            # Envia os dados de volta para o cliente
            self.conn.send(data)

        # Fecha a conexão
        self.conn.close()


if __name__ == '__main__':
    server = Server()
    # server.set_pid_parameters(10, 1, 0.5, 0, PID_FLAG=True)
    server.set_pid_parameters()
    server.run()
