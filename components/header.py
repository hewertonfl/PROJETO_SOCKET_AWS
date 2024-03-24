from dash import html


def header():
    return html.Div(
        className="header",
        children=[
            html.H1("Dashboard"),
            html.P("Monitoramento de temperatura e umidade"),
        ],
    )
