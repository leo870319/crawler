import requests
import json
import get_key

get_key.run()
f = open("city.json","r")
j = open("forcast.json","w")

cities = json.load(f)
apikey = "pjskPH6AJ2U3RwgBk6cPGF0AMl2tiybh"

for x in cities:
    q = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/'+x['key'], params={'apikey':apikey})
    content = q.json()
    print(content)
    x['forecast'] = content 

data = json.dumps(cities)

j.write(data)

j.close()
f.close()

    
    
