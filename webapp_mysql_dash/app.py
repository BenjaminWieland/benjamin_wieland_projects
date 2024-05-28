# Project: Create a web app with the framework "dash" that visualizes certain data from a mySQL data base.
# The data base is set up as an AWS RDS.
# The code is to be run inside the same AWS account as the one in which the RDS exists, so no extra AWS login
# procedures are necessary.

import boto3
from botocore.exceptions import ClientError
import json
import pandas as pd
from sqlalchemy import create_engine
from dash import Dash, html, dcc
import plotly.express as px

# Retrieve the data base credentials through a secret created with AWS KMS

def get_secret():

    secret_name = "webapp-secret-key"
    region_name = "eu-central-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return secret
 
secret_dict = json.loads(get_secret())

# Establish the connection to sqlalchemy with create_engine and define the desired search queries: 
#     1: Number of orders per month,
#     2: The top 10 customers with the most orders,
#     3: The top 10 sales reps,
#     4: Number of customers per country.

engine = create_engine(f'mysql+mysqldb://{secret_dict["username"]}:{secret_dict["password"]}@{secret_dict["host"]}:{secret_dict["port"]}/classicmodels')
distribution_orders = pd.read_sql("SELECT COUNT(orderNumber) as numberOrders, orderDate FROM orders GROUP BY date_format(orderDate, '%%Y-%%m');", engine)
best_customers = pd.read_sql("SELECT COUNT(orderNumber) as numberOrders, customerName FROM orders LEFT JOIN customers on orders.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY COUNT(orderNumber) DESC LIMIT 10;", engine)
busy_sales_rep = pd.read_sql("SELECT firstName AS salesRepFirstName, lastName  AS salesRepLastName, COUNT(customerNumber) AS numberCustomers FROM employees LEFT JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber GROUP BY lastName ORDER BY COUNT(customerNumber) DESC LIMIT 10;", engine)
customer_overview = pd.read_sql("SELECT COUNT(customerNumber) AS numberCustomers, country FROM customers GROUP BY country ORDER BY COUNT(country) DESC;", engine)

# Create dash app with visualizations with pandas

def create_app(table, x_label, y_label, H1_title):
    app = Dash(__name__)
    df = pd.DataFrame(table)
    fig = px.bar(df, x=x_label, y=y_label)
    app.layout = html.Div(children=[
    html.H1(children=H1_title),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ])

    app.run_server(debug=True)
    exit

# Test the dash app

if __name__ == "__main__":
    create_app(distribution_orders, "orderDate", "numberOrders", "Number of orders by date")
    create_app(best_customers, "customerName", "numberOrders", "Number of orders by customer")
    create_app(busy_sales_rep, "salesRepLastName", "numberCustomers", "Number of customers by Sales Rep")
    create_app(customer_overview, "country", "numberCustomers", "Number of customers by country")