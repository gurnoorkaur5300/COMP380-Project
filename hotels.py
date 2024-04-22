import requests

class Hotels:
    API_KEY = "a591c48a33mshfb582683b7ba583p1da719jsnbfb2f45d508a"
    API_HOST = "hotels-com-free.p.rapidapi.com"
    BASE_URL = "https://hotels-com-free.p.rapidapi.com"

    @staticmethod
    def get_destination_id(city_name):
        url = f"{Hotels.BASE_URL}/suggest/v1.7/json"
        headers = {
            'X-RapidAPI-Key': Hotels.API_KEY,
            'X-RapidAPI-Host': Hotels.API_HOST
        }
        querystring = {"query": city_name, "locale": "en_US"}
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            try:
                return data['suggestions'][0]['entities'][0]['destinationId']
            except (IndexError, KeyError):
                return None
        else:
            return None
    

    @staticmethod
    def fetch_hotels(destination_id, checkin, checkout):
        url = f"{Hotels.BASE_URL}/srle/listing/v1/brands/hotels.com"
        headers = {
            'X-RapidAPI-Key': Hotels.API_KEY,
            'X-RapidAPI-Host': Hotels.API_HOST
        }
        querystring = {
            "destinationId": destination_id,
            "checkIn": checkin,
            "checkOut": checkout,
            "rooms": "1",
            "locale": "en_US",
            "currency": "USD"
        }
        response = requests.get(url, headers=headers, params=querystring)
        return response.json()

    @staticmethod
    def fetch_hotel_details(property_id):
        url = f"{Hotels.BASE_URL}/pde/property-details/v1/hotels.com/{property_id}"
        headers = {
            'X-RapidAPI-Key': Hotels.API_KEY,
            'X-RapidAPI-Host': Hotels.API_HOST
        }
        querystring = {
            "rooms": "1",
            "locale": "en_US",
            "currency": "USD",
            "include": "neighborhood"
        }
        response = requests.get(url, headers=headers, params=querystring)
        return response.json()