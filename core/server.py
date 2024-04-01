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

        self.set_pid_parameters()

    def calculate_VP(self, PID_OUTPUT):
        # G = 2/(2s+3)
        VP = 0.7408*self.previous_VP + 0.1728 * PID_OUTPUT
        return VP

    def convert_vp_output_to_json(self, message):
        message = {"VP_OUTPUT": str(message)}
        message = json.dumps(message)
        return message

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
            data = self.conn.recv(1024).decode()

            # Se não houver dados, encerra o loop
            if not data:
                break
            # Converte os dados recebidos em um objeto JSON
            try:
                dado = json.loads(data)
            except json.JSONDecodeError:
                print("Erro ao decodificar JSON")
                continue

            # Extrai o valor de 'PID_OUTPUT' dos dados
            data = dado["PID_OUTPUT"]

            # Converte 'PID_OUTPUT' em um float
            data = float(data)

            # Calcula o valor de VP com base em data
            VP = self.calculate_VP(data)

            print(f"VP no servidor: {VP}")

            # Convert o valor de VP para JSON e o codifica em bytes
            data = self.convert_vp_output_to_json(VP).encode()

            # Se usar o frontend, descomente a linha abaixo
            yield VP
            # Envia os dados de volta para o cliente
            self.conn.send(data)

        # Fecha a conexão
        self.conn.close()


if __name__ == '__main__':
    server = Server()
    server.set_pid_parameters(setpoint=25, Kp=1, Ki=0.5, Kd=0, PID_FLAG=True)
    server.run()
