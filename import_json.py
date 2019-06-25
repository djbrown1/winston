#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:55:13 2019

@author: cenapantel
"""

import json
from urllib.request import urlopen
#get string name
s = "test"
url = "https://dictionaryapi.com/api/v3/references/collegiate/json/%s?key=d1e7be76-e74e-408a-b349-493d72db5cfb" %s
print(url)
data = urlopen(url) 
output = json.loads(data.read())
print(output)
with open('test.json', 'w') as json_file:  
    json.dump(output, json_file)