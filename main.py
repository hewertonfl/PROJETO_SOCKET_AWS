import dash
from dash import dcc
from dash import html
from components import sidebar, main_content, header
from local.server import Server
import threading
import numpy as np
from collections import deque
import time

output_VP = deque(maxlen=100)
pid_parameters = None
reset = False


class VpGetter:
    def __init__(self):
        self.server = Server()
        self.vp = self.server.run()

    def output(self):
        global output_VP, reset
        while True:
            try:
                if reset:
                    output_VP = []
                    self.server.set_pid_parameters(
                        pid_parameters['setpoint'], pid_parameters['Kp'], pid_parameters['Ki'], pid_parameters['Kd'], PID_FLAG=True)
                    reset = False
                else:
                    vp = next(self.vp)
                    print(f"VP: {vp}")
                    vp = float(vp)
                    time.sleep(1)
                    output_VP.append(vp)
            except StopIteration:
                break


class HomePage:
    def __init__(self):
        self.external_stylesheets = ["./assets/style.css"]
        self.app = dash.Dash(
            __name__, external_stylesheets=self.external_stylesheets)
        self.graph_style = {"flex": 1, "min-width": 700}
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = html.Div(
            children=[
                header.header(),
                sidebar.sidebar(),
                main_content.mainContent(),
                html.Div(id='hidden-div', style={'display': 'none'}),
                dcc.Interval(id='interval_component',
                             n_intervals=0, interval=1000),
            ], className="dash_container"
        )

    def setup_callbacks(self):
        @self.app.callback(
            dash.Output("grafico-controle", "figure"),
            dash.Input('interval_component', 'n_intervals'),
        )
        def update_graph(n):
            x_output = np.arange(len(output_VP))

            y_output = np.array(output_VP)

            # Atualiza os gráficos
            grafico_controle = {
                "data": [
                    {
                        "x": x_output,
                        "y": y_output,
                        "type": "line",
                    }
                ],
                "layout": {
                    "title": "Sistema de controle",
                    "xaxis": {"title": "Tempo (s)"},
                    "yaxis": {"title": "Variável de processo"},
                },
            }

            return grafico_controle

        @self.app.callback(
            dash.Output('hidden-div', 'children'),
            [dash.Input('submit-val', 'n_clicks')],
            [dash.State('setpoint', 'value'),
             dash.State('Kp', 'value'),
             dash.State('Ki', 'value'),
             dash.State('Kd', 'value')]
        )
        def update_output(n_clicks, setpoint, Kp, Ki, Kd):
            global pid_parameters, reset
            if n_clicks > 0:
                pid_parameters = {"setpoint": setpoint,
                                  "Kp": Kp, "Ki": Ki, "Kd": Kd}
                print(
                    f"Setpoint: {pid_parameters ['setpoint']}, Kp: {Kp}, Ki: {Ki}, Kd: {Kd}")
                reset = True
                return 0
            else:
                return 0

    # @staticmethod
    def run(self):
        port = 8050
        print(f"Dashboard rodando em: http://127.0.0.1:{port}")
        self.app.run_server(debug=True)


if __name__ == "__main__":
    # vp_getter = VpGetter()
    # home_page = HomePage()
    # t1 = threading.Thread(target=vp_getter.output)
    # t2 = threading.Thread(target=home_page.run)

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
    HomePage().run()
