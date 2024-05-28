# Project: Create an online shop app with the framework "dash" that visualizes certain key facts
# concerning the shop and its product sales.
# The data are stored in an AWS DynamoDB data base. The code is to be run inside the same AWS account
# so no additional AWS login procedures are required. In this file, functions from another .py-file ("queries_dynamodb")
# are used. 

from queries_dynamodb import *
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import boto3
import json
import pandas as pd
import datetime
import plotly.express as px
import plotly.io as pio

# Set up the dynamoDB connection

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

# Create the layout of the dash app

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        dcc.Input(id='product_name', type='text', value='leeres Produkt'),
        dcc.Input(id='quantity', type='number', value=0),
        dcc.Input(id='first_name', type='text', value='leerer Vorname'),
        dcc.Input(id='last_name', type='text', value='leerer Nachname'),
        dcc.Input(id='country', type='text', value='leeres Land'),
        dcc.Input(id='email', type='text', value='leere E-mail-Adresse')
    ]),
    dbc.Row([
        html.Div(id='output-state')
    ]),
    dbc.Row([
        html.Button(id='submit-button-state', n_clicks=0, children='Submit')
    ]),
    dbc.Row([
       dcc.Graph(id='plant-sales', figure=get_plant_graph()) 
    ]),
    dbc.Row([
        dbc.Col(dcc.Interval(id='interval', interval=10000))
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='plant-output')),
                dbc.CardImg(src= app.get_asset_url('spider-plant.png'), style={'width' : '150px', 'height' : '150px'})
            ])
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='book-output')),
                dbc.CardImg(src= app.get_asset_url('book.png'), style={'width' : '150px', 'height' : '150px'})
            ])
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='shoes-output')),
                dbc.CardImg(src= app.get_asset_url('sneakers.png'), style={'width' : '150px', 'height' : '150px'})
            ])
        ])
    ])
])

# Callback function to take in a new order and save it to the dynamoDB

@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('product_name', 'value'),
              State('quantity', 'value'),
              State('first_name', 'value'),
              State('last_name', 'value'),
              State('country', 'value'),
              State('email', 'value')
)
def new_order(n_clicks, product_name, quantity, first_name, last_name, country, email):
    if n_clicks > 0:
        order_date = datetime.date.today().strftime("%Y%m%d")
        order_list = [email, order_date, product_name, quantity, first_name, last_name, country]
        df = pd.DataFrame([order_list])
        df.columns = ['customerID', 'orderID', 'product', 'quantity', 'firstname', 'lastname', 'country']
        response = table.put_item(
            Item={
                'customerID' : email, 
                'orderID' : order_date,
                'product' : product_name,
                'quantity' : quantity,
                'firstname' : first_name,
                'lastname' : last_name,
                'country' : country
        })
        return "Your input has been submitted"

# Callback functions to display the total number of orders of the three product groups

@app.callback(Output('plant-output', 'children'),
            Input('interval', 'n_intervals')
)            
def get_plant(interval):
    total_plants = sum(get_productorders_timerange('plant')["quantity"])
    return "Summe plant: ", total_plants
    
@app.callback(Output('book-output', 'children'),
            Input('interval', 'n_intervals')
)            
def get_book(interval):
    total_books = sum(get_productorders_timerange('book')["quantity"])
    return "Summe book: ", total_books
    
@app.callback(Output('shoes-output', 'children'),
            Input('interval', 'n_intervals')
)            
def get_shoes(interval):
    total_shoes = sum(get_productorders_timerange('shoes')["quantity"])
    return "Summe shoes: ", total_shoes

if __name__ == '__main__':
    app.run_server(debug=True)