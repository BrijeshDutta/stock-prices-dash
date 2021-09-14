import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import yfinance as yf
import datetime

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(id='graph-with-slider'),
#     dcc.Slider(
#         id='year-slider',
#         min=df['year'].min(),
#         max=df['year'].max(),
#         value=df['year'].min(),
#         marks={str(year): str(year) for year in df['year'].unique()},
#         step=None
#     )
# ])


# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[df.year == selected_year]

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig


app = dash.Dash()

# Basic Bar chat in Dash
# app.layout = html.Div(
#     children=[
     
#     html.H1(children='Dash Trading'),
#     dcc.Graph(
        
#         id='example',
#         figure={
#             'data':[
                
#                 {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
#                 {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
#                 ], 
#             'layout':{
#                 'title': 'Basic Dash Example'
#             }
            
#         }
#     )   
#     ]
    
    
# )

# Interactive User Interface - Data Visualization GUIs with Dash and Python p.2




app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='TSLA', type='text'),
    html.Div(id='output-graph'),


])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    
    #define the ticker symbol
    tickerSymbol = 'TSLA'
    #get data on this ticker
    tickerData = yf.Ticker(input_data)
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=start, end=end)

    tickerDf.reset_index(inplace=True)
    tickerDf.set_index("Date", inplace=True)
    
    
    return  dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': tickerDf.index, 'y': tickerDf.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
