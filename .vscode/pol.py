from win10toast import ToastNotifier # import class win10toast from module ToastNotifier
import requests
from time import sleep
import json


#notifier.show_toast("Sample Notification", "You are learning at Tutorialspoint", duration = 25)

getapidata = requests.get('https://corona.lmao.ninja/v2/countries/ghana')

apidatatojson = getapidata.json()

#print(apidatatojson)

text = 'Confirmed Cases: {} \nTotal Deaths: {} \n Total Recoveries: {}'.format(apidatatojson["cases"],apidatatojson["deaths"], apidatatojson["recovered"])

while True:

    notifier = ToastNotifier() #instantiate the class
    notifier.show_toast("Ghana Covid-19 status update:", text, duration=30)
    sleep(280)   