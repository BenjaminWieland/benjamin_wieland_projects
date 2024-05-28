# Helper functions for the dash app that will use these functions as methods.
# The data which the functions access are stored in an AWS DynamoDB data base.

import boto3
import json
import pandas as pd
from boto3.dynamodb.conditions import Key
import datetime
import plotly.express as px
import plotly.io as pio
import plotly.offline as offline

client = boto3.client('dynamodb')

# Get product orders at a certain time

def get_productorders_timerange(product_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Orders')
    response = table.query(IndexName = 'Products', KeyConditionExpression= Key('product').eq(product_name))
    response_dict = response["Items"]
    df = pd.DataFrame(response_dict)
    df['orderID'] = pd.to_datetime(df['orderID'], format='%Y%m%d')
    return df

# Get total number of orders for the three categories: shoes, books and plants

def get_total_shoes():
    total_shoes = sum(get_productorders_timerange('shoes')["quantity"])
    return total_shoes
 
def get_total_books():
    total_books = sum(get_productorders_timerange('book')["quantity"])
    return total_books

def get_total_plants():
    total_plants = sum(get_productorders_timerange('plant')["quantity"])
    return total_plants
    
# Create a graph for the number of orders of plants at a certain date

def get_plant_graph():
    plant_df = get_productorders_timerange('plant')[['quantity', 'orderID']].drop(12)
    plant_figure = px.area(
        plant_df,
        x="orderID",
        y="quantity",
        color_discrete_sequence=['blue'],
        labels={
            "orderID" : "Bestelldatum",
            "quantity" : "Bestellmenge"
        })
    return plant_figure

# Test the functions
    
if __name__=="__main__":
    test = get_productorders_timerange('plant')[['quantity', 'orderID']].drop(12)
    figure = px.area(
        test,
        x="orderID",
        y="quantity",
        color_discrete_sequence=['blue'],
        labels={
            "orderID" : "Bestelldatum",
            "quantity" : "Bestellmenge"
        })
    offline.plot(figure, filename='test_graph2.html', image='png')