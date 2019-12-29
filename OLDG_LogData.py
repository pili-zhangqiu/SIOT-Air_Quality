# Import Google Sheets API libraries
from __future__ import print_function  
from googleapiclient.discovery import build  
from httplib2 import Http  
from oauth2client import file, client, tools  
from oauth2client.service_account import ServiceAccountCredentials  
import datetime

import time
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Import the function reading the ADC values from both MQ135 sensors (Air Quality)
from ADS1x15_read import ADCread

# Import the library reading the DHT22 values (Temperature and Humidity)
import DHT22_read import DHTread

#==================================================================================

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# My Spreadsheet ID ... See google documentation on how to derive this
MY_SPREADSHEET_ID = '1x-PEGT76a5Roh4-HkeA8lpDTRqaZw-RSTeOhviL27ys'

def update_sheet(sheetname, AirQy0, AirQy1, temp0, hum0, temp1, hum1):  
    """update_sheet method:
       appends a row of a sheet in the spreadsheet with the 
       the latest temperature, pressure and humidity sensor data
    """
    # authentication, authorization step
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    
    # Call the Sheets API, append the next row of sensor data
    # values is the array of rows we are updating, its a single row
    values = [ [ str(datetime.datetime.now()), 
        AirQy0 , temp0, hum0, AirQy1, temp1, hum1 ] ]
    body = { 'values': values }
    
    # call the append API to perform the operation
    result = service.spreadsheets().values().append(
                spreadsheetId=MY_SPREADSHEET_ID, 
                range=sheetname + '!A1:H1',
                valueInputOption='USER_ENTERED', body=body).execute()                     

#==================================================================================

def main():  
  
    while True:
        
        # Read air quality values from the MQ135 sensors
        ADC_values = ADCread()
        print (ADC_values)

        ADC0 = ADC_values[0]    # Air Quality Inside
        ADC1 = ADC_values[1]    # Air Quality Outside
        
        # Read temperature and humidity values from the DHT22 sensors
        DHT_pin0 = 23
        DHT_pin1 = 24

        # Print values on the command prompt
        print ('Air Quality: (Inside) %f PPM' % ADC0)
        print ('Air Quality: (Outside) %f PPM' % ADC1)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))       
        print ('-' *30)

        update_sheet("Sheet1", ADC0, ADC1)
        time.sleep(60)

if __name__ == '__main__':  
    main()
