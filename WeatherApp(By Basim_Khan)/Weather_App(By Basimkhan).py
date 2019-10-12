import tkinter as tk
from tkinter import font
import requests

root = tk.Tk()


# Apikey = Use your own apikey    # to get both of these create an acount on openweathermap.org
# Apicall = and api call also


def button_function(entry):
    print("you pressed me ?: ", entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humid = weather['main']['humidity']
        wind = weather['wind']['speed']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \nHumidity: %s \nWind Speed: %s' % (
            name, desc, temp, humid, wind)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = "Again Use your own api key"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

back_image = tk.PhotoImage(file="./landscape.png")
back_label = tk.Label(root, image=back_image)
back_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#66d9ff", bd=5)
frame.place(relheight=0.1, relwidth=0.75, relx=0.5, rely=0.1, anchor="n")

button = tk.Button(frame, text="Get Weather!", bg="#e6e6e6", fg="black", font=('Courier', 9),
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.8, rely=0.1, relheight=0.8, relwidth=0.2)

entry = tk.Entry(frame, bg="white", fg="black", font=('Courier', 16), )
entry.place(relx=0.01, rely=0.1, relheight=0.8, relwidth=0.75)

another_frame = tk.Frame(root, bg="#66d9ff", bd=10)
another_frame.place(relheight=0.6, relwidth=0.75, relx=0.5, rely=0.25, anchor="n")

label = tk.Label(another_frame, font=('Courier', 18))
label.place(relheight=1, relwidth=1)

root.mainloop()
