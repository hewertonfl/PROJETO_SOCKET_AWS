import socket
from controller import Controller
import matplotlib.pyplot as plt
import numpy as np
import json


class Client:
    def __init__(self):
        host = socket.gethostname()
        # host = "3.213.7.49"
        port = 5000
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.output = []
        self.controller = Controller()
        self.setpoint = 20
        self.Kp = 1
        self.Ki = 0.5
        self.Kd = 0
        self.VP = 0

    def plot(self):
        t = np.arange(len(self.output))
        plt.plot(t, self.output)
        plt.title('VP vs Time')
        plt.xlabel('Time')
        plt.ylabel('VP')
        plt.grid(True)
        plt.show()

    def load_pid_settings(self, data):
        if data['setpoint'] != self.setpoint or data['Kp'] != self.Kp or data['Ki'] != self.Ki or data['Kd'] != self.Kd:
            self.setpoint = data['setpoint']
            self.Kp = data['Kp']
            self.Ki = data['Ki']
            self.Kd = data['Kd']
            print(
                f"Setpoint: {self.setpoint}, Kp: {self.Kp}, Ki: {self.Ki}, Kd: {self.Kd}")

    def convert_pid_to_json(self, message):
        message = {"PID_OUTPUT": str(message)}
        message = json.dumps(message)
        return message

    def run(self):
        message = self.controller.PID(
            self.setpoint, self.Kp, self.Ki, self.Kd, self.VP)
        counter = 0
        while message != 0:
            # Convert the PID message to JSON and encode it
            message_json = self.convert_pid_to_json(message)
            message_bytes = json.dumps(message_json).encode("utf-8")

            # Send the message
            self.client_socket.send(message_bytes)

            # Receive the response
            data = self.client_socket.recv(1024).decode()

            VP = json.loads(data)
            if VP["PID_FLAG"]:
                self.load_pid_settings(VP)
                message = self.controller.PID(
                    self.setpoint, self.Kp, self.Ki, self.Kd, self.VP)
                continue
            elif not VP["PID_FLAG"]:
                continue
            else:
                VP = float(VP["PID_OUTPUT"])
                self.output.append(VP)

                # Update the message with the new PID
                message = self.controller.PID(
                    self.setpoint, self.Kp, self.Ki, self.Kd, VP)
                counter += 1

            # if counter > 100:
            #     break

        self.client_socket.close()  # close the connection
        self.plot()


if __name__ == '__main__':
    Client().run()
