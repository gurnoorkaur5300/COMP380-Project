import requests

class Hotels:
    """
    Provides methods for interacting with hotel-related data.
    :author: Gurnoor Kaur
    :version: 1.0

    Attributes:
        API_KEY: API key for authentication with the hotel data provider.
        API_HOST: The host name for the hotel data API.
        BASE_URL: The base URL for the hotel data API.

    Methods:
        get_destination_id(city_name): Returns the destination ID for a given city name.
        fetch_hotels(destination_id, checkin, checkout): Fetches hotel data for the specified destination and dates.
        fetch_hotel_details(property_id): Fetches detailed information about a specific hotel property.
    """
    
    API_KEY = "a591c48a33mshfb582683b7ba583p1da719jsnbfb2f45d508a"
    API_HOST = "hotels-com-free.p.rapidapi.com"
    BASE_URL = "https://hotels-com-free.p.rapidapi.com"

    @staticmethod
    def get_destination_id(city_name):
        """
        Retrieves the destination ID for a given city name.

        Args:
            city_name: The name of the city to retrieve the destination ID for.

        Returns:
            The destination ID if found, otherwise None.
        """
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
        """
        Fetches hotel data for the specified destination and dates.

        Args:
            destination_id: The destination ID for the city.
            checkin: The check-in date in YYYY-MM-DD format.
            checkout: The check-out date in YYYY-MM-DD format.

        Returns:
            The hotel data as a JSON object.
        """
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
        """
        Fetches detailed information about a specific hotel property.

        Args:
            property_id: The ID of the hotel property to fetch details for.

        Returns:
            Detailed information about the hotel as a JSON object.
        """
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
