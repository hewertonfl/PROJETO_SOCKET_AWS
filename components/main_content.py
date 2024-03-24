from dash import html
from .graphs import grafico_controle


def mainContent():
    return html.Div(
        className="content",
        children=[
            html.Div([
                html.Div(
                    html.Div(grafico_controle, className="grafico")),
            ]),
        ]
    )


()
