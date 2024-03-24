from dash import html
from dash import dcc


def sidebar():
    return html.Div(
        className="sidebar",
        children=[
            html.Span([html.H1("Sistema de controle", style={'text-align': 'center'}),
                       html.P("Controlador das nuvens", style={'display': 'flex', 'justify-content': 'center'})], style={'display': 'flex', 'flex-direction': 'column', "margin-top": "5rem"}),
            html.Div([
                html.H3("Parâmetros do PID", style={'margin-bottom': '10px'}),
                html.P("Setpoint: ", className="PID-text"),
                dcc.Input(id='setpoint', type='number',
                          value=20, className="input-style"),
                html.P("Constante Kp:", className="PID-text"),
                dcc.Input(id='Kp', type='number', value=1,
                          className="input-style"),
                html.P("Constante Ki:", className="PID-text"),
                dcc.Input(id='Ki', type='number', value=0.5,
                          className="input-style"),
                html.P("Constante Kd:", className="PID-text"),
                dcc.Input(id='Kd', type='number', value=0,
                          className="input-style"),
                html.Button('Enviar', id='submit-val', n_clicks=0, style={
                            'margin-bottom': '10px', 'width': '100%'}, className="PID-button"),
            ],
                id='output-div',
                style={'display': 'flex', 'flex-direction': 'column',
                       'justify-content': 'start', 'align-items': 'center', 'width': '90%'},
                className="PID-box"
            ),
        ], style={'width': '25%'},
    )
