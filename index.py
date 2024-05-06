from geopy.geocoders import GoogleV3

# Initialize the Google geocoder with your API key
geolocator = GoogleV3(api_key='YOUR_API_KEY')

# Location you want to geocode
location = "Statue of Liberty"

# Getting latitude and longitude
address = geolocator.geocode(location)

# Printing address, latitude, and longitude
print("Location Address:", address)
print("Latitude:", address.latitude)
print("Longitude:", address.longitude)