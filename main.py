import requests
import json

# import get_key
#
# get_key.run()
f = open("forcast.json", "r")

cities = json.load(f)

apikey = "pjskPH6AJ2U3RwgBk6cPGF0AMl2tiybh"
url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"
for x in cities:
    q = requests.get(
        url + x["key"],
        params={"apikey": apikey},
    )
    content = q.json()
    print(content)
    array = x["forecast"]
    array += content
    x["forecast"] = array

data = json.dumps(cities)

j = open("forcast.json", "w")
j.write(data)

j.close()
f.close()
