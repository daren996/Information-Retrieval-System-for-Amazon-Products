"""
Configurations

"""
import os
import json

root_path = "../Amazon/IR"
# root_path = "."

clean_rule = r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt | rt |\n'

stopwords_file = root_path + "/stopwords/google_stopwords.txt"

data_ori_path = root_path + "/input/data_origin/"
data_path = root_path + "/input/doc_data/"
data_cat_path = root_path + "/input/doc_cat_data/"

D_path = root_path + "/input/index_data/D"
word_set_path = root_path + "/input/index_data/word_list"
word2id_map_path = root_path + "/input/index_data/word2id_map"
index_path = root_path + "/input/index_data/index"
doc_length_path = root_path + "/input/index_data/doc_length"

fileid_path = root_path + "/input/index_data/fileid.txt"

datafile2id = {"bestseller": 1, "ClothingShoesJewelry": 2, "FoodHardware": 3}  # use this to generate doc_id
id2datafile = {"1": "bestseller", "2": "ClothingShoesJewelry", "3": "FoodHardware"}

magnitude = 100000000

cat2id = {
    "Movies & TV": 1,
    "Entertainment Collectibles": 2,
    "Appliances": 3,
    "Software": 4,
    "Clothing, Shoes & Jewelry": 5,
    "Apps & Games": 6,
    "Digital Music": 7,
    "Video Games": 8,
    "Grocery & Gourmet Food": 9,
    "Gift Cards": 10,
    "Baby": 11,
    "Automotive": 12,
    "Arts, Crafts & Sewing": 13,
    "Amazon Devices & Accessories": 14,
    "Sports Collectibles": 15,
    "Amazon Launchpad": 16,
    "Kindle Store": 17,
    "Patio, Lawn & Garden": 18,
    "Office Products": 19,
    "Computers & Accessories": 20,
    "Kitchen & Dining": 21,
    "Tools & Home Improvement": 22,
    "Home & Kitchen": 23,
    "Toys & Games": 24,
    "Electronics": 25,
    "Camera & Photo": 26,
    "Sports & Outdoors": 27,
    "Health & Household": 28,
    "Books": 29,
    "Pet Supplies": 30,
    "CDs & Vinyl": 31,
    "Cell Phones & Accessories": 32,
    "Baby Products": 33,
    "Musical Instruments": 34,
    "Magazine Subscriptions": 35,
    "Back to results": 36,
    "Beauty & Personal Care": 37,
    "Industrial & Scientific": 38,
    }

if __name__ == '__main__':
    cat_arr = set()
    doc_files = os.listdir(data_path)
    for filename in doc_files:
        with open(data_path + filename, "r") as input_file:
            for line in input_file.readlines():
                obj = json.loads(line.strip())
                cat = obj["cat"]
                if cat['1'] not in cat_arr:
                    cat_arr.add(cat['1'])
    count = 1
    for cat in cat_arr:
        print("\"" + cat + "\": " + str(count) + ",")
        count += 1

    out_file_arr = []
    for i in range(1, len(cat2id) + 1):
        out_file_arr.append(open(data_cat_path + str(i), "w"))
    for filename in doc_files:
        with open(data_path + filename, "r") as input_file:
            for line in input_file.readlines():
                obj = json.loads(line.strip())
                cat = obj["cat"]["1"]
                cat_id = cat2id[cat]
                out_file_arr[cat_id - 1].write(line.strip() + "\n")
