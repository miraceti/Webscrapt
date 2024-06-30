from flet import *
# from geopy.geocoders import Nominatim
import webbrowser

webbrowser.register("firefox", None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Mozilla Firefox\firefox.exe"))

def main(page:Page):
    
	
	# you_search = TextField(label="you search")
	def searchstreetview(e):
		# address = you_search.value
		# AND NOW CONVERT YOU ADDRESS NAME TO latitude
		# LONGITUDE
		# geolocator = Nominatim(user_agent="myapp")
		# location = geolocator.geocode(address)
		# lat,lon = location.latitude,location.longitude

		# NOW PARSING LAT AND LON TO URL STREETVIEW
		url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+from+ps+where+default_flag=1&format=json"
		# page.snack_bar = SnackBar(
		# 	Text("opening browser",size=30),
		# 	bgcolor="green"
		# 	)
		# page.snack_bar.open = True

		# AND NOW OPEN AUTOMATICALY BROWSER
		
		
		# AND REDIRECT YOU TO URL STREETVIEW
		webbrowser.get("firefox").open(url)

		# AND YOU NOT RUN flet main.py WITH ROOT
		# YOU MUST USE USER NO ROOT


		page.update()


	page.add(
	Column([
	# Text("input streetview location",
	# 	weight="bold",size=20
	# 	),
	# you_search,
	ElevatedButton("search streetview",
		bgcolor="blue",color="white",
		on_click=searchstreetview
		)

	])
		)

app(target=main)