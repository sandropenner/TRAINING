import requests 


class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name 
        self.lat = lat 
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=4180f61c9ddbc2bd0b0809e89ed11252")
        except:
            print("No Internet Connection...")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):

        print(f"Currently it is {self.temp}°C outside")
        print(f"Today's high: {self.temp_max}°C")
        print(f"Today's low: {self.temp_min}°C")


my_city = City("Oxbow", 49.2272, -102.1695)     
my_city.temp_print()   
print(my_city.response_json)

vacation_city = City("Mitchell", 49.5342, -96.7620)
vacation_city.temp_print()  