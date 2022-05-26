import requests
import urllib.parse


def find(meal_type,location):
	
	meal_type = urllib.parse.quote(meal_type)
	location = urllib.parse.quote(location)
	
	url = f"https://api.foursquare.com/v3/places/search?query={meal_type}&near={location}&sort=DISTANCE"

	print("\n\n"+url+"\n\n")

	headers = {
		"Accept": "application/json",
		"Authorization": "fsq3JWESDZttTqNG9BzfhQiUFOaQRee0g1SeJjTUychdAV4="
	}

	response = requests.get(url, headers=headers)

	print(response.text)
	

if __name__ == '__main__':

	
	find("cachaça", "terminal central, campinas, sp, brazil")
