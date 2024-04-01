import socket
from controller import Controller
import matplotlib.pyplot as plt
import numpy as np
import json


class Client:
    def __init__(self):
        host = socket.gethostname()
        host = "54.198.239.48"
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

    def convert_pid_output_to_json(self, message):
        message = {"PID_OUTPUT": str(message)}
        message = json.dumps(message)
        return message

    def send_message(self, PID_FLAG=False, response=None):
        if PID_FLAG:
            self.load_pid_settings(response)
        message = self.controller.PID(
            self.setpoint, self.Kp, self.Ki, self.Kd, self.VP)
        message = self.convert_pid_output_to_json(message)
        self.client_socket.send(message.encode())

    def run(self):
        counter = 0
        while True:
            # Receive the response
            response = self.client_socket.recv(1024).decode()
            response_dict = json.loads(response)

            # Check if the response is a PID message
            if "PID_FLAG" in response_dict.keys():
                self.send_message(response=response_dict,
                                  PID_FLAG=response_dict["PID_FLAG"])
                counter += 1
                continue

            # Load the PID output
            PID_RESPONSE = response_dict["VP_OUTPUT"]
            self.VP = float(PID_RESPONSE)

            # Save a list of the VP values
            self.output.append(self.VP)

            # Send the response to the server
            self.send_message(response=self.VP)

            counter += 1

            # if counter > 100:
            #     break

        self.client_socket.close()  # close the connection
        self.plot()


if __name__ == '__main__':
    Client().run()
