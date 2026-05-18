import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
df = pd.read_csv("data/formatted_sales_data.csv")
df = df.sort_values(by="date")
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Soul Foods: Pink Morsel Sales Visualizer', style={'textAlign': 'center'}),
    dcc.RadioItems(
        id='region-filter',
        options=['North', 'East', 'South', 'West', 'All'],
        value='All', 
        inline=True,
        style={'textAlign': 'center', 'marginBottom': '20px'}
    ),
    dcc.Graph(id='sales-line-chart')
])
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region.lower()]
    fig = px.line(filtered_df, x='date', y='sales', title=f'Pink Morsel Sales - {selected_region.title()} Region')
    return fig
if __name__ == '__main__':
    app.run(debug=True)