"""
This is a small script that handles result.txt

@author: Darren
"""

import json


name_arr = set()
item_arr = {}
count = 0
with open("amazon/result/result.txt") as input_file:
    for line in input_file.readlines():
        count += 1
        json_obj = json.loads(line.strip())
        name = json_obj['name']
        url = json_obj['url']
        cat1 = json_obj['cat']["1"]
        cat2 = json_obj['cat']["2"]
        if name not in name_arr:
            name_arr.add(name)
            if cat1 is None or cat2 is None:
                print(count, line)
            if cat1 not in item_arr:
                item_arr[cat1] = {}
            if cat2 not in item_arr[cat1]:
                item_arr[cat1][cat2] = []
            item_arr[cat1][cat2].append({'name': name, 'url': url})

# how many first and second categories
print(len(item_arr))
for cat1 in item_arr:
    print(cat1, len(item_arr[cat1]))
