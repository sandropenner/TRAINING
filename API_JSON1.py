import requests 
import tkinter 
from tkinter import ttk, messagebox

class City:
    def __init__(self, name, units):
        self.name = name 
        self.units = units
        self.get_coordinates()
        self.get_temp()

    def get_coordinates(self):
        try:
            coordinate_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.name}&limit=1&appid=4180f61c9ddbc2bd0b0809e89ed11252")
            self.coordinate_json = coordinate_response.json()[0]
            self.lat = self.coordinate_json["lat"]
            self.lon = self.coordinate_json["lon"]
        except:
            messagebox.showerror("Invalid input, try again:")


    def get_temp(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=4180f61c9ddbc2bd0b0809e89ed11252")
            self.response_json = response.json()
            self.temp = self.response_json["main"]["temp"]
            self.temp_min = self.response_json["main"]["temp_min"]
            self.temp_max = self.response_json["main"]["temp_max"]
        except:
            messagebox.showerror("No Internet Connection...")


    def temp_print(self):
        unit_label = "C" if self.units == "metric" else "F"
        weather_info = f"Currently it is {self.temp}°{unit_label} in {self.name}\n"
        weather_info += f"Today's high: {self.temp_max}°{unit_label}\n"
        weather_info += f"Today's low: {self.temp_min}°{unit_label}"
        messagebox.showinfo("Weather Information", weather_info)


def get_weather():
    name = city_entry.get()
    units = unit_var.get()
    if name and units:
        city = City(name, units)
        city.temp_print()

root = tkinter.Tk()
root.title("Weather App")
root.geometry("310x170")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10), background="yellow", foreground="black")
style.configure("TRadiobutton", font=("Arial", 10))

label = ttk.Label(root, text="City and Country Code (e.g., Oxbow,CA):")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

city_entry = ttk.Entry(root, font=("Arial", 10))
city_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

unit_var = tkinter.StringVar()
metric_rb = ttk.Radiobutton(root, text='Metric', variable=unit_var, value='metric')
imperial_rb = ttk.Radiobutton(root, text='Imperial', variable=unit_var, value='imperial')
metric_rb.grid(row=2, column=0)
imperial_rb.grid(row=2, column=1)

submit_button = ttk.Button(root, text="Submit", command=get_weather)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()