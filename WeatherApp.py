import asyncio
import tkinter as tk
from tkinter import ttk
import python_weather
import threading

# Get the weather

async def get_weather(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)
    return weather

# Get city name 

def on_button_click():
    city = entry.get()
    
    def async_task():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        weather = loop.run_until_complete(get_weather(city))
        loop.close()
        
        if weather:
            temperature = weather.temperature
            result_var.set(f"The current temperature in {city} is {temperature} degrees Fahrenheit.")
        else:
            result_var.set("Could not retrieve weather data. Please check the city name.")

    thread = threading.Thread(target=async_task)
    thread.start()

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Set the size of the window
root.geometry("400x300")

frm = ttk.Frame(root, padding=10)
frm.place(relx=0.5, rely=0.5, anchor="center")

entry = ttk.Entry(frm, width=30)
entry.pack(padx=10, pady=10)

button = ttk.Button(frm, text="Get Weather", command=on_button_click)
button.pack(padx=10, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(frm, textvariable=result_var)
result_label.pack(padx=10, pady=10)

root.mainloop()
