# Sensing & IoT - Air Quality Device Project
This project aims to explore the benefits of IoT home devices to better inform and encourage users to move towards a healthier lifestyle. This can be done through web app that visualizes different real-time graphs on air quality. From this UI, the user can appreciate the big difference between indoors and outdoors air quality and it can alert the user of when they should, for instance, open the window.

[<img src= "https://github.com/pili-zhangqiu/SIOT-Air_Quality/blob/master/img/LinkBanner.jpg" width="500">](https://www.pilarzhangqiu.com/siot-breathe)

## Files:
The **main files** are: 
- **Hardware_Scripts folder**: contains the scripts needed to read data from the sensors:
    - **Temperature and humidity**:
      - DHT22_read.py: Script to read data from the DHT22 sensor (digital temperature and humidity sensor)
    - **Air quality**:
      - ADS1x15_read.py: Data from the MQ-135 sensor (air quality sensor) is received through ADC.
      - MQ135_Calibrate.py: Calibrates the PPM air quality data received. You can learn more about CO2 levels [here](https://www.engineeringtoolbox.com/co2-comfort-level-d_1024.html)

    - **Actuator**:
      - Energenie_Control.py: Turns on the air purifier if the air quality reaches a threshold
![CircuitDiagram](https://github.com/pili-zhangqiu/SIOT-Air_Quality/blob/master/img/CircuitDiagram.jpg)

- **Google_Data_Recorder folder**: contains the necessary scripts to write data from the sensors to an online Google Sheets-
    -  Main Script: GLog.py
    -  **Please, bear in mind that you will need to retrieve your _client_secret.json_ file**. Due to confidentiality reasons, this file is not displayed in this Github.
    -  **Links of interest:**
        - Spreadsheet Tutorial: http://www.whatimade.today/log-sensor-data-straight-to-google-sheets-from-a-raspberry-pi-zero-all-the-python-code/?fbclid=IwAR1KB3eKgikrl87bONCU7gI7-nIvOin2d264GQd-ZP2u1ZJhFzjey_ScrU4
        - oauth2client (solved https://oauth2client.readthedocs.io/en/latest/)
       
- **WebApp folder**: contains the webapp script, controlling both the data visualisation and backend data retrieval from the Google Sheet.
    - Main Script: index.html
    - This web app displays the data in the form of Chart JS graphs. To run this file, Apache (web server software) was used.
    - Here is a video showcasing the WebApp functionalities:
 
[<img src= "https://github.com/pili-zhangqiu/SIOT-Air_Quality/blob/master/img/LinkVideo.PNG" width="500">](https://vimeo.com/680045192)

