import json
import re
import collections
import sys

#read in raw data
raw_objs_string = open(sys.argv[1]).read()
txt = "".join(raw_objs_string.split())
retrieved_strings = ['{'+x+'}' for x in txt.strip('{}').split('}{')]

data = collections.defaultdict(list)
flag = 0
cityfinal = collections.defaultdict(list)
cities_dict={}
cities_list=[]
finaldict={}

for i in retrieved_strings:
    data = json.loads(i)
    for k,v in data.items():
#checking if the user is android or iOS or windows users using the filed "a"
        if k == "a":
            if ("android" in v) or ("Android" in v):
                flag=1
            if "ios" in v.lower() or "iphone" in v.lower() or "Mac" in v.lower() or "iPad" in v.lower():
                flag=2
            if "Windows" in v or "windows" in v:
                flag=3
#checking the timezone for the user,and incrementing the value for each type of user for the particular timezone
        if k=="tz":
            if flag==1:
                v1 = v.split("/")
                if v1[0] == "America" or v1[0] == "america":
                    cityfinal[v1[1]].append("android")
                    flag = 0
            if flag==2:
                v1 = v.split("/")
                if v1[0] == "America" or v1[0] =="america":
                    cityfinal[v1[1]].append("ios")
                    flag=0
            if flag==3:
                v1 = v.split("/")
                if v1[0] == "America" or v1[0] =="america":
                    cityfinal[v1[1]].append("windows")
                    flag=0


for k,v in cityfinal.items():
    finaldict[k] = max(v)


for k,v in finaldict.items():
        cities_dict[k] = v
        cities_list.append(cities_dict)
        cities_dict={}



#json file which is used to visualize using D3
with open('users.json', 'w') as fp:
    json.dump(cities_list, fp)




