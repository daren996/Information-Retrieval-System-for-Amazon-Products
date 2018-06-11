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

datafile2id = {"bestseller": 1, "ClothingShoesJewelry": 2}  # use this to generate doc_id
id2datafile = {"1": "bestseller", "2": "ClothingShoesJewelry"}

magnitude = 100000000

cat2id = {
    "Sports & Outdoors": 1,
    "Toys & Games": 2,
    "Industrial & Scientific": 3,
    "Kitchen & Dining": 4,
    "CDs & Vinyl": 5,
    "Clothing, Shoes & Jewelry": 6,
    "Sports Collectibles": 7,
    "Grocery & Gourmet Food": 8,
    "Beauty & Personal Care": 9,
    "Amazon Launchpad": 10,
    "Apps & Games": 11,
    "Amazon Devices & Accessories": 12,
    "Books": 13,
    "Software": 14,
    "Video Games": 15,
    "Magazine Subscriptions": 16,
    "Appliances": 17,
    "Office Products": 18,
    "Tools & Home Improvement": 19,
    "Electronics": 20,
    "Entertainment Collectibles": 21,
    "Arts, Crafts & Sewing": 22,
    "Kindle Store": 23,
    "Pet Supplies": 24,
    "Health & Household": 25,
    "Patio, Lawn & Garden": 26,
    "Musical Instruments": 27,
    "Movies & TV": 28,
    "Camera & Photo": 29,
    "Computers & Accessories": 30,
    "Digital Music": 31,
    "Cell Phones & Accessories": 32,
    "Home & Kitchen": 33,
    "Gift Cards": 34,
    "Automotive": 35,
    "Baby": 36,
    "Back to results": 37,
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
