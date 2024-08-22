import requests
import json

# response = requests.get('https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners/7813/locations')


#ask for user input so to retrieve the pay out partner name if they know it
# name = input("Insert pay out partner name: ")

# iterate through various dicts so to match pay-out-partner


#We iterate through these dictionaries to find pay out partner
def find_pay_partner():
    response = requests.get('https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners')
    
    if response.status_code == 200:
        pay_out_partner_name = input("Insert pay out partner name: ")
        all_entries = response.json()
        
        for element in all_entries["items"]:
            if element["name"] == pay_out_partner_name:
                found_partner = element
                print("Found:", found_partner)
                return found_partner
        print("Pay out partner not found.")
    else:
        print("Failed to retrieve data.")
    return found_partner

def grab_guid(guid):
    name = guid["guid"]
    print(name)

def find_address():
    pass   

def main():
    var = find_pay_partner()
    grab_guid(var)
main()
    


# payOutPartnerGuid = response.json()["items"][3]["guid"]
# print(payOutPartnerGuid)
