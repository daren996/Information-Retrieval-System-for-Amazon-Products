"""
to convert
"""

import os
import django
import json
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Amazon.settings")
django.setup()

from Database.models import Product
import nltk
import re
import IR.conf
from IR.index import Index
from IR.search import Search




# 把json文件中的数据导入数据库中
# filename_list = os.listdir("../../IR/input/doc_data/")
# filename_list.remove("bestseller")
# filename_list.remove("ClothingShoesJewelry")
# print(filename_list)
# for filename in filename_list:
#     with open("../../IR/input/doc_data/" + filename, "r") as input_file:
#         for line in input_file.readlines():
#             obj = json.loads(line.strip())
#             url = obj["url"]
#             cat = obj["cat"]
#             cat_str = ""
#             for c in cat.items():
#                 cat_str += c[1] + " "
#             cat_str = cat_str.strip()
#             name = obj["name_ori"]
#             P_id = obj["id"]
#             if P_id % 100 == 0:
#                 print(filename, P_id, P_id % 1000000 / 32654)
#             product = Product(P_id=P_id, title=name, url=url, category=cat_str)
#             if len(obj["picture"]) > 0:
#                 product.photo = obj["picture"][0]
#             if len(obj["star"]) > 0:
#                 product.star = obj["star"][0] if type(obj["star"]) == list else obj["star"]
#             if obj["price"] != "":
#                 product.price = obj["price"]
#             product.save()


# 把照片等信息加进去
# filename_list = os.listdir("../../IR/input/doc_data/")
# filename_list.remove("bestseller")
# filename_list.remove("ClothingShoesJewelry")
# filename_list.remove("FoodHardware")
# print(filename_list)
# for filename in filename_list:
#     with open("../../IR/input/doc_data/" + filename, "r") as input_file:
#         for line in input_file.readlines():
#             obj = json.loads(line.strip())
#             P_id = obj["id"]
#             if P_id % 100 == 0:
#                 print(filename, P_id, P_id % 1000000 / 32654)
#             product = Product.objects.get(P_id=P_id)
#             if len(obj["picture"]) > 0:
#                 product.photo = obj["picture"][0]
#             if obj["price"] != "":
#                 product.price = obj["price"]
#             if len(obj["star"]) > 0:
#                 product.star = obj["star"][0] if type(obj["star"]) == list else obj["star"]
#             print(product.star)
#             product.save()


# 看有没有重复
# id_arr = set()
# list = Product.objects.all()
# print(len(list))
# for i in range(len(list)):
#     P_id = list[i].P_id
#     if P_id not in id_arr:
#         id_arr.add(P_id)
#     else:
#         print("duplicate: ", P_id)
#         list[i].delete()


# list = Product.objects.all()
#
# print(len(list))
# print(list[0].P_id)
# product = Product.objects.get(P_id=100000001)
# print(product.P_id)


# P_id = 2
# title = "Title"
# url = "http://amazon.com/"
# category = "Category"
# price = "999"
# star = "5 out of 5 stars"
# description = "Description"
# details = "Details"
#
# obj = Product(P_id=P_id, title=title, url=url, category=category, price=price, star=star, description=description, details=details)
# obj.save()



# Product.objects.all().delete()