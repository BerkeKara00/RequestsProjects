import requests
from tkinter import *
from PIL import ImageTk, Image

API_KEY = 'apiKey'



def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(city):
    weather_data = fetch_weather_data(city)
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        humidity = main_data['humidity']
        temperature = main_data['temp'] - 273.15
        weather_description = weather_data['weather'][0]['description']

        result_label.config(
            text=f"City: {city}\nTemperature: {temperature:.2f}°C\nHumidity: {humidity}%\nWeather description: {weather_description.capitalize()}"
        )
    else:
        result_label.config(text="City not found. Please try again.")

    # Şehir adını temizle
    entry1.delete(0, END)



def on_button_click(event=None):
    city = entry1.get()
    display_weather_data(city)

window = Tk()
window.title("Hava Durumu Uygulaması")

window.minsize(width=300, height=300)
window.config(pady=75)

# Resmi oranlarını korumak ve Canvas'ı resmin boyutuna uygun ayarlamak için bir ölçek faktörü kullanalım
scale_factor = 0.5  # Ölçek faktörünü ayarlayabilirsiniz

# Resmi aç
image = Image.open("default.png")

# Resmi ölçekle
width, height = image.size
width = int(width * scale_factor)
height = int(height * scale_factor)
resized_image = image.resize((width, height), Image.BICUBIC)  # ANTI_ALIAS özelliği yerine BICUBIC kullanıldı.

# Resmi Tkinter PhotoImage formatına çevir
tk_image = ImageTk.PhotoImage(resized_image)

# Canvas'ı resmin boyutlarına uygun olarak oluştur
canvas = Canvas(window, width=width, height=height)
canvas.create_image(0, 0, anchor=NW, image=tk_image)
canvas.pack()

label1 = Label(text="Enter the name of the city: ")
label1.config()
label1.pack(pady=10)

entry1 = Entry()
entry1.pack()

button = Button(text="Get Weather", command=on_button_click)
button.pack(pady=20)

result_label = Label(window, text="")
result_label.pack(pady=10)

# ENTER tuşuna basıldığında on_button_click fonksiyonunu çağır
entry1.bind("<Return>", on_button_click)

window.mainloop()
