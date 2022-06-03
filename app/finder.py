import requests
import urllib.parse

def find(meal_type,location):
	
	meal_type = urllib.parse.quote(meal_type)
	location = urllib.parse.quote(location)
	
	url = f"https://api.foursquare.com/v3/places/search?query={meal_type}&near={location}&sort=DISTANCE"

	headers = {
		"Accept": "application/json",
		"Authorization": "fsq3JWESDZttTqNG9BzfhQiUFOaQRee0g1SeJjTUychdAV4="
	}

	response = requests.get(url, headers=headers)
	res_dict = response.json()
	

	restaurants = []

	for i in range(len(res_dict['results'])):

		restaurant_id = res_dict['results'][i]['fsq_id']
		restaurant_id = urllib.parse.quote(restaurant_id)
		photo_url = f"https://api.foursquare.com/v3/places/{restaurant_id}/photos?classifications=indoor%2Coutdoor"
		photo_response = requests.request("GET", photo_url, headers=headers)
			
		if photo_response.status_code == 200:
			photo_response = photo_response.json()
			try:
				photo_link = photo_response[0]['prefix'] + "300x300" + photo_response[0]['suffix']
			except:
				photo_link = "https://www.rosacomercial.com.br/app/templates/default/images/nao-disponivel.jpg"
		else:
			photo_link = "https://www.rosacomercial.com.br/app/templates/default/images/nao-disponivel.jpg"		

		place_dict = {
		"name": res_dict['results'][i]['name'],
		"address": res_dict['results'][i]['location']['formatted_address'],
		"photo": photo_link
		}

		restaurants.append(place_dict)


	return restaurants