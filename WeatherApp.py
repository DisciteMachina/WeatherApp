import requests 

def get_weather(city):
    API_KEY = '10ac6730f61a55a788f95583c5e1d6e5'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}"
    response = requests.get(base_url)
     
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temperature = main['temp']

        print(f"City: {data['name']}")
        print(f"Temperature: {round(temperature)}°C")
        print(f"Weather: {weather}")
    else:
        print("City not found.")
         
     
city_name = input("Enter city name: ")
get_weather(city_name)

