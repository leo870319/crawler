import requests
import json


# generate city list
def run():
    j = open("CityCountyData.json", "r")
    data = json.load(j)
    list = []
    for x in data:
        list.append(x["CityEngName"])

    # get city key

    apikey = "pjskPH6AJ2U3RwgBk6cPGF0AMl2tiybh"
    url = "http://dataservice.accuweather.com/locations/v1/TW/search"

    citykey = []
    f = open("city.json", "w")
    for x in list:
        query = {"apikey": apikey, "q": x, "details": "yes"}

        q = requests.get(url, params=query)
        data = q.json()
        try:
            citykey.append({"name": x, "key": data[0]["Key"]})
        except:
            citykey.append({"name": x, "key": ""})

    f.write(json.dumps(citykey))

    f.close()


#
#
# p = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-7DEBAB12-3501-48EA-8E17-CE913507A987&limit=10&sort=time')
# print(p.content)


# for x in q.content:
#     print(x['ID'])
