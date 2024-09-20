import requests 
import tkinter as tk


def get_weather(city):
    API_KEY = ':P'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}"
    response = requests.get(base_url)
     
    if response.status_code == 200:
        city = city
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temperature = main['temp']

        show_data(temperature, weather, city)
        print(f"City: {data['name']}")
        print(f"Temperature: {round(temperature)}°F")
        print(f"Weather: {weather}")
    else:
        print("City not found.")
         


# Main Window
root = tk.Tk()
root.title("Input Box Example")
root.geometry("300x200") 

# Label
label = tk.Label(root, text="Enter City:")
label.pack(pady=10)

# Input Box
entry = tk.Entry(root)
entry.pack(pady=10)

def store_input():
    global city
    city = entry.get()
    get_weather(city)
    
def show_data(temperature, weather, city):
    result_label.config(text=f"City: {city}\nTemperature: {temperature}°F\nWeather: {weather}")


    
button = tk.Button(root, text="Submit", command=store_input)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)



root.mainloop()



