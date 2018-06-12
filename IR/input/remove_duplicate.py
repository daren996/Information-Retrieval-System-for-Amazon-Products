"""
remove duplicate

"""

import os
import json

# remove duplicate
# dir_path = "./doc_data/"
# dir_path = "./data_origin/"
# url_set = set()
# doc_files = os.listdir(dir_path)
# doc_files.remove("bestseller")
# doc_files.remove("ClothingShoesJewelry")
# print(doc_files)
# for filename in doc_files:
#     out_file = open(dir_path + filename+"_new", "w")
#     with open(dir_path + filename, "r") as input_file:
#         for line in input_file.readlines():
#             json_obj = json.loads(line.strip())
#             url = json_obj['url']
#             if url not in url_set:
#                 url_set.add(url)
#                 out_file.write(json.dumps(json_obj) + "\n")
#     out_file.close()
    # os.remove(dir_path + filename)
    # os.renames(dir_path + filename+"_new", dir_path + filename)


# dir_path = "./data_origin/"
# url_set = set()
# doc_files = ["Amazon_data_hardware.json", "Amazon_data_Food.json"]
# for filename in doc_files:
#     out_file = open(dir_path + filename + "_new", "w")
#     with open(dir_path + filename, "r") as input_file:
#         for line in input_file.readlines():
#             json_obj = json.loads(line.strip())
#             url = json_obj['url']
#             if url not in url_set:
#                 url_set.add(url)
#                 new_obj = {
#                     "name": json_obj["title"],
#                     "url": json_obj["url"],
#                     "cat": {"1": "Grocery & Gourmet Food"} if len(json_obj["cat"]) == 1
#                     else {"1": json_obj["cat"][0].strip(), "2": json_obj["cat"][1].strip()} if len(json_obj["cat"]) == 2
#                     else {"1": json_obj["cat"][0].strip(), "2": json_obj["cat"][1].strip(),
#                           "3": json_obj["cat"][2].strip()} if len(json_obj["cat"]) >= 3
#                     else {"1": "Grocery & Gourmet Food"},
#                     "price": json_obj["price"],
#                     "picture": [url[0] for url in json.loads(json_obj["picture"][0]).items()] if len(
#                         json_obj["picture"]) > 0 else [],
#                     "star": json_obj["star"][0] if len(json_obj["star"]) > 0 else ""
#                 }
#                 print(new_obj)
#                 out_file.write(json.dumps(new_obj) + "\n")
