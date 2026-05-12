import dash 
from dash import dcc, html
import plotly.express as px
import pandas as pd
df=pd.read_csv("data/formatted_sales_data.csv")
df= df.sort_values(by="date")
fig = px.line(df, x='date', y='sales', title='pink morsell sales before and after price increase')
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children= 'soul foods: pink morsell sales visualizer', style={'textAlign':'center'}),
    dcc.Graph(
        id= 'sales-line-chart',
        figure = fig
    )
])
if __name__=='__main__':
    app.run(debug=True)
