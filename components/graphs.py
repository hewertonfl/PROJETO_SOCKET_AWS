from dash import dcc

# Cria os gráficos
grafico_controle = dcc.Graph(
    id="grafico-controle",
    responsive=True,
    className="graph",
)
