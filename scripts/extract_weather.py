import requests

# List of cities with their coordinates
cities = [
    {"name": "London", "lat": 51.5072, "lon": -0.1276},
    {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904},
    {"name": "Manchester", "lat": 53.4808, "lon": -2.2426},
]


def fetch_weather():
    base_url = "https://api.open-meteo.com/v1/forecast"

    # Store all weather data in a list
    all_data = []

    # loop through each city and fetch weather data
    for city in cities:
        params = {
            "latitude": city["lat"],
            "longitude": city["lon"],
            "hourly": "temperature_2m,precipitation",
        }

        # GET request to fetch weather data for the city
        response = requests.get(base_url, params=params)
        data = response.json()

        # attach city name
        data["city"] = city["name"]

        all_data.append(data)

    # Return the list of weather data for all cities
    return all_data


if __name__ == "__main__":
    data = fetch_weather()
    print(data)
