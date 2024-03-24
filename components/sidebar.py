from dash import html
from dash import dcc


def sidebar():
    return html.Div(
        className="sidebar",
        children=[
            html.Span([html.H1("Sistema de controle", style={'text-align': 'center'}),
                       html.P("Controle PID de nível", style={'display': 'flex', 'justify-content': 'center'})], style={'display': 'flex', 'flex-direction': 'column', 'margin-bottom': '50%'}),
            html.Div([
                html.H3("Parâmetros do PID", style={'margin-bottom': '10px'}),
                html.P("Setpoint: ", className="input-style"),
                dcc.Input(id='setpoint', type='number',
                          placeholder='Setpoint', className="input-style"),
                html.P("Constante Kp:", className="input-style"),
                dcc.Input(id='Kp', type='number', placeholder='Kp',
                          className="input-style"),
                html.P("Constante Ki:", className="input-style"),
                dcc.Input(id='Ki', type='number', placeholder='Ki',
                          className="input-style"),
                html.P("Constante Kd:", className="input-style"),
                dcc.Input(id='Kd', type='number', placeholder='Kd',
                          className="input-style"),
                html.Button('Enviar', id='submit-val', n_clicks=0, style={'margin-bottom': '10px', 'width': '100%'}),],
                id='output-div',
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'start', 'align-items': 'center', 'width': '80%'}),
            # html.Img(src="./assets/images/ifes_logo.png",
            #          style={"width": "40%", 'position': 'absolute', 'bottom': '10%'}),
        ],
    )
