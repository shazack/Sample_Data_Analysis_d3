# -*- coding: utf-8 -*-
import json
import re
import collections
import sys
from urlparse import urlparse
#read in raw data
raw_objs_string = open(sys.argv[1]).read()
txt = "".join(raw_objs_string.split())
retrieved_strings = ['{'+x+'}' for x in txt.strip('{}').split('}{')]

links = collections.defaultdict()
data = collections.defaultdict(list)



for i in retrieved_strings:
    data = json.loads(i)
    #getting the top level domain name
    for k,v in data.items():
        if k == "u":
            url = v
            hostname = urlparse(url).hostname
            hostname = urlparse(url).hostname.split(".")
            if hostname[1] in links:
                 #preprocessing of text
                if len(hostname[1]) >2 and (hostname[1].find("com") == -1) and (hostname[1].find("org") == -1):
                    links[hostname[1]]+=1
            else:
                url = v
                hostname = urlparse(url).hostname
                hostname = urlparse(url).hostname.split(".")
                #preprocessing of text
                if len(hostname[1]) >2 and (hostname[1].find("com") == -1) and (hostname[1].find("org") == -1):
                    links[hostname[1]]=1
url_dict={}
url_list=[]
for k,v in links.items():
        url_dict["text"]=k
        url_dict["size"]=v
        url_list.append(url_dict)
        url_dict={}



#putting it in json format to visualize using D3
with open('urls.json', 'w') as fp:
    json.dump(url_list, fp)