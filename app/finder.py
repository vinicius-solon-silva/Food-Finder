import requests

def findARestaurant(mealType,location):

	headers = {
        "Accept": "application/json",
        "Authorization": "fsq3JWESDZttTqNG9BzfhQiUFOaQRee0g1SeJjTUychdAV4="
    }
	
	url = f"https://api.foursquare.com/v3/places/search?query={mealType}&near={location}&sort=DISTANCE"
	response = requests.request("GET", url, headers=headers)
	response = response.json()

	try:
		restaurant_id = response['results'][0]['fsq_id']
		restaurant_name = response['results'][0]['name']
		restaurant_address = response['results'][0]['location']['address']
	except Exception as e:
		return None

	photo_url = f"https://api.foursquare.com/v3/places/{restaurant_id}/photos?classifications=indoor%2Coutdoor"
	photo_response = requests.request("GET", photo_url, headers=headers)
		
	if photo_response.status_code == 200:
		photo_response = photo_response.json()
		try:
			photo_link = photo_response[0]['prefix'] + "300x300" + photo_response[0]['suffix']
		except:
			photo_link = "https://ss3.4sqi.net/img/categories_v2/arts_entertainment/themepark_120.png"
	else:
		photo_link = "https://ss3.4sqi.net/img/categories_v2/arts_entertainment/themepark_120.png"

	place_dict = {
		"name": restaurant_name,
		"address": restaurant_address,
		"photo": photo_link
	}

	return place_dict
