import requests 
import tkinter as tk
from PIL import Image, ImageTk

def get_weather(city):
    API_KEY = '10ac6730f61a55a788f95583c5e1d6e5'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}"
    response = requests.get(base_url)
     
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temperature = main['temp']

        show_data(temperature, weather, city)
    else:
        result_label.config(text='City not found.')

# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300") 

# Label
label = tk.Label(root, text="Enter City:")
label.pack(pady=10)

# Input Box
entry = tk.Entry(root)
entry.pack(pady=10)

image_label = None

def store_input():
    global city
    city = entry.get()
    get_weather(city)

def show_data(temperature, weather, city):
    result_label.config(text=f"City: {city.title()}\nTemperature: {round(temperature)}°F\nWeather: {weather}")
    
    global image_label
    if image_label:
        image_label.pack_forget()

    if "rain" in weather:
        image_path = "images/rainy.png"
    elif "clear" in weather:
        image_path = "images/sunny.png"
    elif "cloud" in weather:
        image_path = "images/cloudy.png"
    elif "snow" in weather:
        image_path = "images/snowy.png"
    elif "thunderstorm" in weather:
        image_path = "images/stormy.png"
    else:
        image_path = None
        
    if image_path:
        image = Image.open(image_path)
        
        image = image.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        
        image_label = tk.Label(root, image=photo)
        image_label.image = photo  
        image_label.pack()


# Button
button = tk.Button(root, text="Submit", command=store_input)
button.pack(pady=10)

# Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
