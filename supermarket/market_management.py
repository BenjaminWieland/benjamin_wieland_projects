# Manage a supermarket with the classes "Supermarket", "Employee" and "Product"
import json
import pandas as pd
from supermarket import *
import csv

with open("products.csv", "r") as fh:
    next(fh)
    lines = fh.readlines()
products = [i.split(";") for i in lines]

with open("employees.csv", "r") as fh:
    next(fh)
    lines = fh.readlines()
employees = [i.split(";") for i in lines]

my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")
my_supermarket.employees = [i for i in employees]
my_supermarket.products = [i for i in products]

# Give current number of employees
num_employees = len(my_supermarket.employees)
print(f'{my_supermarket.supermarket_name} hat aktuell {num_employees} Mitarbeiter')

# Give most expensive product
max_price_prod = max(my_supermarket.products, key= lambda x : float(x[3]))
print(f'Das teuerste Produkt im {my_supermarket.supermarket_name} ist {max_price_prod[1]}.')

# Give average price of the products
prices = [float(i[3]) for i in my_supermarket.products]
average_price = sum(prices) / len(prices)
print(f'Ein Produkt im {my_supermarket.supermarket_name} kostet im Durchschnitt {round(average_price, 2)} Euro.')

# Give number of products for every category
num_food = len([i for i in my_supermarket.products if i[2] == "food"])
num_drinks = len([i for i in my_supermarket.products if i[2] == "drinks"])
num_others = len([i for i in my_supermarket.products if i[2] == "others"])
print(f'Es gibt {num_food} Produkte in der Kategorie food, {num_drinks} Produkte in der Kategorie drinks und {num_others} in der Kategorie others.')

# Give the name of the oldest employee
oldest_employee = max(my_supermarket.employees, key = lambda x : int(x[3]))
print(f'Der älteste Mitarbeiter heißt {oldest_employee[1]}.')