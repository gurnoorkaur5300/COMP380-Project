import csv
import os

class Hotels:
    @staticmethod
    def get_hotels_by_location(location):
        # Map location names to CSV filenames
        location_to_csv = {
            "New York": "newyork.csv",
            "Los Angeles": "losangeles.csv",
            "Chicago": "chicago.csv",
            "Houston": "houston.csv",
            "Miami": "miami.csv"
        }
        
        # Get the appropriate CSV filename
        csv_filename = location_to_csv.get(location)
        if not csv_filename:
            return []
        
        # Open the CSV file corresponding to the selected location
        hotels = []
        csv_path = os.path.join("hotelsData", csv_filename)
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                hotels.append({
                    'name': row['Name'],
                    'price_range': row['Price Range'],
                    'description': row['Description'],
                    'amenities': row['Amenities'].split(", "),
                    'image_path': os.path.join("hotelsData", row['Image Path'])
                })
        return hotels
