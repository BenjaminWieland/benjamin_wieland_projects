# Create the software for a ticket machine

import json
print("Herzlich willkommen bei ihrer Bahn, sie haben folgende Fahrkarten zur Auswahl:")
with open("tickets.json", "r") as file:
    automat = json.load(file)
    index = 0
    for value in automat["tickets"]:
        print(index, value["name"])
        index += 1

ticket_input = int(input("Bitte geben sie die entsprechende Zahl für die gewünschte Fahrkarte ein: "))
while ticket_input < 0 or ticket_input >= len(automat["tickets"]):
    print("Ungültige Auswahl.")
    ticket_input = int(input("Bitte geben sie die entsprechende Zahl für die gewünschte Fahrkarte ein: "))
ticket_category = automat["tickets"][ticket_input]["name"]
ticket_price = automat["tickets"][ticket_input]["price"]

print(f'\nSie haben das Ticket {ticket_category} gewählt. Der Preis beträgt {ticket_price} Euro.')
print("Dieser Automat akzeptiert folgende Münzen und Geldscheine:")
for value in automat["accepted_cash"]:
    print(value, "Euro")

total = 0
diff = ticket_price - total
while total < ticket_price:
    money_input = int(input(f'\nBitte werfen sie eine Münze/einen Geldschein ein, es fehlen noch {diff} Euro: '))
    if money_input in automat["accepted_cash"]:
        print(f'Danke für {money_input} Euro.')
        total = total + money_input
        diff = ticket_price - total
    else:
        print(f'{money_input} ist ein ungültiges Nominal.')
if total > ticket_price:
    change = total - ticket_price
    print(f'\nIhr Restgeld beträgt {change} Euro.')
    print("Danke für ihren Einkauf und gute Fahrt.")
else:
    print("Danke für Ihren Einkauf und gute Fahrt.")