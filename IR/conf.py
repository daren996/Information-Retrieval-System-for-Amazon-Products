"""
Configurations

"""
import os
import json

clean_rule = r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt | rt |\n'

stopwords_file = "./stopwords/google_stopwords.txt"

data_ori_path = "./input/data_origin/"
data_path = "./input/doc_data/"
data_cat_path = "./input/doc_cat_data/"

D_path = "./input/index_data/D"
word_set_path = "./input/index_data/word_list"
word2id_map_path = "./input/index_data/word2id_map"
index_path = "./input/index_data/index"
doc_length_path = "./input/index_data/doc_length"

fileid_path = "./input/index_data/fileid.txt"

datafile2id = {"bestseller": 1, "ClothingShoesJewelry": 2}  # use this to generate doc_id
id2datafile = {"1": "bestseller", "2": "ClothingShoesJewelry"}

magnitude = 100000000

cat2id = {
    "Amazon Launchpad": 1,
    "Computers & Accessories": 2,
    "CDs & Vinyl": 3,
    "Sports & Outdoors": 4,
    "Apps & Games": 5,
    "Kitchen & Dining": 6,
    "Clothing, Shoes & Jewelry": 7,
    "Health & Household": 8,
    "Camera & Photo": 9,
    "Kindle Store": 10,
    "Office Products": 11,
    "Books": 12,
    "Amazon Devices & Accessories": 13,
    "Entertainment Collectibles": 14,
    "Movies & TV": 15,
    "Patio, Lawn & Garden": 16,
    "Appliances": 17,
    "Video Games": 18,
    "Grocery & Gourmet Food": 19,
    "Automotive": 20,
    "Baby": 21,
    "Musical Instruments": 22,
    "Arts, Crafts & Sewing": 23,
    "Pet Supplies": 24,
    "Back to results": 25,
    "Beauty & Personal Care": 26,
    "Industrial & Scientific": 27,
    "Sports Collectibles": 28,
    "Digital Music": 29,
    "Magazine Subscriptions": 30,
    "Electronics": 31,
    "Cell Phones & Accessories": 32,
    "Home & Kitchen": 33,
    "Gift Cards": 34,
    "Tools & Home Improvement": 35,
    "Toys & Games": 36,
    "Software": 37
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
