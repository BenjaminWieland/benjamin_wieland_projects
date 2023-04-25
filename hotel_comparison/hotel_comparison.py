# Find symmetric difference between two lists
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]
set_list1 = set(list1)
set_list2 = set(list2)
print(type(set_list1))

sym_differences = list(set_list1.symmetric_difference(set_list2))
print(sym_differences)
sym_differences.sort()
print(sym_differences)

print(set(list1).symmetric_difference(set(list2)))

# Find common values in two lists
common_values = (set_list1 & set_list2)
print(common_values)

if (set_list1 & set_list2):
    print(set_list1 & set_list2)
else:
    print("No common elements")

common_values_alt = list(set_list1.intersection(set_list2))
print(common_values_alt)
common_values_alt.sort()
print(common_values_alt)
    
# Compare two hotels to each other
Marriott = {
    "name" : "Marriott",
    "age" : 1999,
    "payment_options" : ["card", "cash", "online"],
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night" : 50,
    "employees" : ["carlo", "maria", "marta", "luis", "fernando"]
}

Hilton = {
    "name" : "Hilton",
    "age" : 1992,
    "payment_options" : ["card", "online"],
    "available_rooms" : [100, 800, 801, 805, 1000, 1001],
    "price_per_night" : 70,
    "employees" : ["artur", "maria", "oliver", "xenia"]
}
# Compare the costs

cost_marriott = 5 * Marriott["price_per_night"]
print(cost_marriott)

cost_hilton = 5 * Hilton["price_per_night"]
print(cost_hilton)

if cost_marriott > cost_hilton:
    cost_difference = cost_marriott - cost_hilton
else:
    cost_difference = cost_hilton - cost_marriott
print(abs(cost_difference))

print(f'Fünf Übernachtungen kosten {cost_marriott} € im Hotel Marriott und {cost_hilton} € im Hotel Hilton. Der Preisunterschied sind {cost_difference} €.')

# Create an e-mail template with a reservation request to both hotels

common_rooms = set(Marriott["available_rooms"]).intersection(set(Hilton["available_rooms"]))
available_rooms = list(common_rooms)
available_rooms_final = ", ".join(str(obj) for obj in available_rooms)
print(available_rooms_final)

print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {available_rooms_final}? Danke.')

print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {str(available_rooms)[1:-1]}? Danke.')

# Give payment options of both hotels

print(f'Im Hotel Marriott gibt es {len(Marriott["payment_options"])} und im Hotel Hilton gibt es {len(Hilton["payment_options"])} Zahlungsmöglichkeiten.')

set_payment_options_marriott = set(Marriott["payment_options"])
print(set_payment_options_marriott)

set_payment_options_hilton = set(Hilton["payment_options"])
print(set_payment_options_hilton)

difference_payment_options = ",".join(set_payment_options_marriott.symmetric_difference(set_payment_options_hilton))
print(difference_payment_options)

print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {difference_payment_options}.')

# Give hotel, where a certain employee works

if "fernando" in Marriott["employees"] and "fernando" not in Hilton["employees"]:
    print("Fernando arbeitet im Hotel Marriott und ich werde dort übernachten.")
else:
    print("Fernando arbeitet im Hotel Hilton und ich werde dort übernachten.")