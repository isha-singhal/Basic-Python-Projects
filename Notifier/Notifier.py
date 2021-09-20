import datetime
import time
import requests
from plyer import notification

covidData=None
try:
	covidData=requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
	print("Data is unable to get fetched.")

if(covidData!=None):
	data=covidData.json()['Success']
	while(True) :
		notification.notify(
			title="COVID19 Stats on {}".format(datetime.date.today()),
			message="Cases: {cases}\nToday cases: {todayCases}\nToday deaths: {todayDeaths}\nTotal active: {active}".format(
				cases=data['cases'],
				todayCases=data['todayCases'],
				todayDeaths=data['todayDeaths'],
				active=data['active']),
			app_icon = r"C:\Users\HP\Pictures\notification.ico",
			timeout=30
		)
		time.sleep(60*2)
