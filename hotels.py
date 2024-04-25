import csv

class Hotels:
    @staticmethod
    def get_hotels_by_location(location):
        # This method fetches hotels from the CSV based on the provided location.
        hotels = []
        with open('hotels.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['location'] == location:
                    hotels.append({
                        'name': row['name'],
                        'price_range': row['price_range'],
                        'amenities': row['amenities'].split(", "),
                        'image_path': row['image_path']
                    })
        return hotels
