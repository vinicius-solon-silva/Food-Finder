import requests
import json


def find(meal_type,location):
	
	meal_type = meal_type.replace("ã", "a")
	meal_type = meal_type.replace("á", "a")
	meal_type = meal_type.replace("à", "a")
	meal_type = meal_type.replace("ç", "c")
	location = location.replace(" ", "%20")
	location = location.replace(",", "%2C")
	location = location.replace(";", "%2C")

	url = f"https://api.foursquare.com/v3/places/search?query={meal_type}&near={location}&sort=DISTANCE"

	# url = "https://api.foursquare.com/v3/places/search?query=cacha%C3%A7a&near=terminal%20central%2C%20campinas%2C%20sp%2C%20brazil&sort=DISTANCE"

	print("\n\n"+url+"\n\n")


	headers = {
		"Accept": "application/json",
		"Authorization": "fsq3JWESDZttTqNG9BzfhQiUFOaQRee0g1SeJjTUychdAV4="
	}

	response = requests.get(url, headers=headers)

	print(response.text)
	

if __name__ == '__main__':

	
	find("cachaça", "terminal central, campinas, sp, brazil")
