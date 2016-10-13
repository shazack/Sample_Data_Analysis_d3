import json
import sys
import os
import collections
countries = collections.defaultdict(list)
li = []
with open('words.json','r') as file:
    data = json.load(file)
    for i in data:
        if i["size"] > 5:
            print i["text"],i["size"]


