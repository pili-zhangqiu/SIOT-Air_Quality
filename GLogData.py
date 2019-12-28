# import many libraries
from __future__ import print_function  
from googleapiclient.discovery import build  
from httplib2 import Http  
from oauth2client import file, client, tools  
from oauth2client.service_account import ServiceAccountCredentials  
import datetime

# Import the function reading the ADC values from both the exterior and interior MQ135 sensors
from ADS1x15_read import ADCread

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# My Spreadsheet ID ... See google documentation on how to derive this
MY_SPREADSHEET_ID = '1x-PEGT76a5Roh4-HkeA8lpDTRqaZw-RSTeOhviL27ys'
temper = 1;


def update_sheet(sheetname, AirQy0, AirQy1):  
    """update_sheet method:
       appends a row of a sheet in the spreadsheet with the 
       the latest temperature, pressure and humidity sensor data
    """

    # authentication, authorization step
    creds = ServiceAccountCredentials.from_json_keyfile_name( 
            'credentials.json', SCOPES)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API, append the next row of sensor data
    # values is the array of rows we are updating, its a single row
    values = [ [ str(datetime.datetime.now()), 
        'AirQy_Inside', AirQy0 , 'AirQy_Outside', AirQy1 ] ]
    body = { 'values': values }
    
    # call the append API to perform the operation
    result = service.spreadsheets().values().append(
                spreadsheetId=MY_SPREADSHEET_ID, 
                range=sheetname + '!A1:G1',
                valueInputOption=value_input_option, body=body).execute()                     


def main():  
    """main method:
       reads the BME280 chip to read the three sensors, then
       call update_sheets method to add that sensor data to the spreadsheet
    """
    
    """    
    bme = bme280.Bme280()
    bme.set_mode(bme280.MODE_FORCED)
    tempC, pressure, humidity = bme.get_data()
    pressure = pressure/100.
    print ('Temperature: %f °C' % tempC)
    print ('Pressure: %f hPa' % pressure)
    print ('Humidity: %f %%rH' % humidity)
    update_sheet("Haifa_outside", tempC, pressure, humidity)
    """
    AirQy_In, AirQy_Out = ADCread()
    print ('Air Quality: (Inside) %f PPM' % AirQy_In)
    print ('Air Quality: (Outside) %f PPM' % AirQy_Out)
    print ('-' *30)
    
    update_sheet("Sheet1", AirQy_In, AirQy_Out)

if __name__ == '__main__':  
    main()
