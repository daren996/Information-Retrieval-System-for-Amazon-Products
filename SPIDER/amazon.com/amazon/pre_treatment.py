import json

file_name = "Amazon_data_Boys"
# file_name = "Amazon_data_Girls"
# file_name = "Amazon_data_Mens"
# file_name = "Amazon_data_Womens"
# file_name = "Amazon_data_Baby"
file_name_out = "Amazon_data"


def get_cat(obj1):
    global cat1
    if len(obj1["cat"]) == 5:
        cat1 = {"1": obj1["cat"][0].strip(),
                "2": obj1["cat"][1].strip(),
                "3": obj1["cat"][2].strip(),
                "4": obj1["cat"][3].strip(),
                "5": obj1["cat"][4].strip()
                }
    elif len(obj1["cat"]) == 4:
        cat1 = {"1": obj1["cat"][0].strip(),
                "2": obj1["cat"][1].strip(),
                "3": obj1["cat"][2].strip(),
                "4": obj1["cat"][3].strip()
                }
    elif len(obj1["cat"]) == 3:
        cat1 = {"1": obj1["cat"][0].strip(),
                "2": obj1["cat"][1].strip(),
                "3": obj1["cat"][2].strip(),
                }
    elif len(obj1["cat"]) == 2:
        cat1 = {"1": obj1["cat"][0].strip(),
                "2": obj1["cat"][1].strip(),
                }
    elif len(obj1["cat"]) == 1:
        cat1 = {"1": obj1["cat"][0].strip(),
                }
    return cat1


count = 0
out_file = open(file_name_out, "a")
with open(file_name + ".json", "r") as in_file:
    for line in in_file.readlines():
        count += 1
        obj = json.loads(line.strip())
        cat = get_cat(obj)
        if len(json.loads(obj["picture"][0])) > 0:
            picture = tuple(json.loads(obj["picture"][0]))
        else:
            picture = []
        new_obj = {"name": obj["title"].strip(),
                   "url": obj["url"],
                   "cat": cat,
                   "price": obj["price"],
                   "picture": picture,
                   "star": obj["star"],
                   }
        print(new_obj)
        out_file.write(json.dumps(new_obj) + "\n")
