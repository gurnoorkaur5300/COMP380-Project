import csv
import os

class Hotels:
    @staticmethod
    def get_hotels_by_location(location):
        hotels = []
        csv_path = 'hotels.csv'  # Path to the CSV file in the main folder
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Location'].lower() == location.lower():
                    hotels.append({
                        'name': row['Name'],
                        'price_range': row['Price Range'],
                        'description': row['Description'],
                        'amenities': row['Amenities'].split(", "),
                        'image_path': row['Image Path']
                    })
        return hotels
