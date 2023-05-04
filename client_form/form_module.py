# a script for a form that receives personal data of financial advisor's client, 
# creates a JSON-file from the data and uploads that file to a save AWS s3 bucket
import json
import boto3

# client input - this can easily be transferred to a GUI and/or a web application
first_name = input("Bitte geben Sie Ihren Vornamen an: ").title()
last_name = input("Bitte geben Sie Ihren Nachnamen an: ").title()
street_name = input("Wie heißt die Straße, in der Sie wohnen? ").title()
street_num = int(input("Ihre Hausnummer? "))
city = input("In welcher Stadt leben Sie? ").title()
telefon = input("Bitte geben Sie Ihre Telefonnummer an: ")
email = input("Bitte geben Sie Ihre E-mail-Adresse an: ")
marital_status = input("Bitte geben Sie Ihren Familienstand an: ")
birth_date = input("Wann sind Sie geboren? ")
occupation = input("Was ist Ihr Beruf? ").title()
yearly_income = int(input("Wie hoch ist Ihr jährliches Nettoeinkommen? "))
net_worth = int(input("Wie hoch ist Ihr Gesamtvermögen? "))


def data_dict():
    """Create dictionary from client inputs"""
    personal_data_dict ={
        "Vorname" : first_name,
        "Nachname" : last_name,
        "Straße" : street_name,
        "Hausnummer" : street_num,
        "Ort" : city,
        "Telefonnummer" : telefon,
        "E-mail" : email,
        "Familienstand" : marital_status,
        "Geburtsdatum" : birth_date,
        "Beruf" : occupation,
        "Nettoeinkommen" : yearly_income,
        "Gesamtvermögen" : net_worth
    }
    return personal_data_dict

def data_json_s3():
    """Create json file from dictionary and upload it to s3 bucket"""
    # create JSON file
    with open("client_data_"+last_name.lower()+"_"+first_name.lower()+".json", "w") as fh:
        json.dump(data_dict(), fh, indent = 4)
    # upload to s3 bucket
    bucket_name = "client-data-private-projects-benjamin-wieland-04-05-2023"
    file_name = "client_data_"+last_name.lower()+"_"+first_name.lower()+".json"
    key_name = "data_input/" + file_name
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, key_name)

if __name__ == '__main__':
    data_json_s3()
