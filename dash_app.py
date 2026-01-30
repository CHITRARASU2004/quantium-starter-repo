import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

app = Dash(__name__)

app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[
        html.H1("Quantium Sales Dashboard"),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        ),

        dcc.Graph(id="sales-graph")
    ]
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == region]

    fig = px.bar(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Sales by Date"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)