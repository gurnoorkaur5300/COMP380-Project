import requests
import http.client
import json

class Hotels:
    
    def fetch_hotels(location, checkin, checkout):
        conn = http.client.HTTPSConnection("hotels-com-free.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "your_api_key",
            'X-RapidAPI-Host': "hotels-com-free.p.rapidapi.com"
        }

        query = f"/path_to_search_endpoint?location={location}&checkin={checkin}&checkout={checkout}&locale=en_US"
        conn.request("GET", query, headers=headers)

        res = conn.getresponse()
        data = res.read()
        conn.close()

        try:
            return json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            return {"error": "Failed to decode response"}

