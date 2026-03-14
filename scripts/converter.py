import json
import csv

with open("forecast1.json") as f:
    data = json.load(f)

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
winds = data["hourly"]["windspeed_10m"]
dirs = data["hourly"]["winddirection_10m"]

with open("weather.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time","temperature","windspeed","winddirection"])

    for i in range(len(times)):
        writer.writerow([times[i],temps[i],winds[i],dirs[i]])

print("CSV created!")