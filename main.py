import requests
import json


# import get_key
#
# get_key.run()
f = open("forecast.json", "r")
j = open("test.json", "w")

cities = json.load(f)

apikey = "W41QyGeqWglFxP74ouh10DOKq4asr8IR"
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
j.write(data)


j.close()
f.close()
