#This file authencates via netbox with your account
import os
import pynetbox

def main_auth():

    #APItoken = os.getenv('netbox_token')
    user_auth_token = input("Enter the token for NetBox (Would ask serval times): ")
    try:
        netbox = pynetbox.api(
            'https://netbox.techops.us-west-2.dev.23andme.net',  
            token = user_auth_token
        )
    except pynetbox.RequestError as e:
        print(e.error)
    
    return netbox
