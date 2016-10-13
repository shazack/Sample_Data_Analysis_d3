import os
import json
import collections
countries=collections.defaultdict(list)
c=[]
with open('words.json','r') as f:
    data = json.load(f)
    for i in data:
        for key, value in i.items():
            if i["size"]  >=30:
                    countries["text"] = i["text"]
                    countries["size"] = i["size"]
                    c.append(countries)
                    countries={}
print c