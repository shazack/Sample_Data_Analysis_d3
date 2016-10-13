import json
import sys
import os
import collections
countries = collections.defaultdict(list)
li = []
with open('geo-parser-output-final.json','r') as file:
    data = json.load(file)
    for k,v in data.items():
        for i in v:
            if i["Geographic_NAME"] not in countries:
                print i["Geographic_NAME"]
                countries["name"] = i["Geographic_NAME"]
            else:
                countries["radius"] = 5
                countries["latitude"] = i["Geographic_LATITUDE"]
                countries["longitude"] = i["Geographic_LONGITUDE"]
                li.append(countries)
                countries={}

print li
with open("si.json",'w') as f:
    json.dump(li,f)