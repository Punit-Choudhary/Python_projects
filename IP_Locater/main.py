import os
import json
import requests
import pandas as pd
import plotly.express as pe
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("API")   # Add your ipgeolocation here

base_url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + str(API) + '&ip='

def triger_api(ip):
    url = base_url + str(ip)

    response = requests.request("GET", url)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
    
if __name__ == "__main__":
    try:
        ip = input("Enter IP address to scan: ")

        print("Scanning the IP...")

        api_response = triger_api(ip)

        continent = api_response['continent_name']
        country = api_response['country_name']
        city = api_response['city']
        district = api_response['district']
        zipcode = api_response['zipcode']
        call_code = api_response['calling_code']
        lat = api_response['latitude']
        lon = api_response['longitude']
        isp = api_response['isp']
        tld = api_response['country_tld']

        
        print(f"""
        # ****************************************************** #
        #               IP Lookup                                #
        #   Developed with \3 by Punit-Choudhary                 
        # ****************************************************** #
        #                                                        
        #  IP address : {ip}                                     
        #  Country : {country}                                   
        #  District : {district}                                 
        #  City : {city}                                         
        #  Zip Code : {zipcode}                                  
        #  Calling code : {call_code}                            
        #  ISP : {isp}                                           
        #  TLD : {tld}                                           
        #  Latitude : {lat}                                      
        #  Longitude : {lon}                                     
        # ****************************************************** #
        """)

    except:
        print("Something fucked up!")
