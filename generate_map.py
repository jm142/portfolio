import folium
from geopy.geocoders import Nominatim


def generate_map(file_path, json_data):
    # Instantiate Folium map (with arbitrary pos/zoom for overview of world)
    travel_map = folium.Map(tiles="cartodbpositron", location=[42, 12], zoom_start=2)

    # Grab cities for each member of the team
    for member in json_data.keys():
        member_cities = json_data[member]['travel']
        # Use Nominatim to get geo coords from city names
        geolocator = Nominatim(user_agent="Flask App")
        for city in member_cities:
            try:
                location = geolocator.geocode(city)
                # Create lat/long array and hold onto it
                coordinate_values = [location.latitude,
                                     location.longitude]
                # Create a new map marker and add it to the map
                folium.Marker(
                    coordinate_values,
                    popup=city,
                    icon=folium.Icon(color=json_data[member]['favorite_color'], icon="plane")
                ).add_to(travel_map)
            except:
                print("Can't find coordinates for " + city)

    # Save generated HTML to template
    travel_map.save(file_path)
