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

datafile2id = {"bestseller": 1}  # use this to generate doc_id
id2datafile = {"1": "bestseller"}

magnitude = 100000000

cat2id = {
    "Tools & Home Improvement": 1,
    "Books": 2,
    "Software": 3,
    "Arts, Crafts & Sewing": 4,
    "Grocery & Gourmet Food": 5,
    "Beauty & Personal Care": 6,
    "Appliances": 7,
    "Musical Instruments": 8,
    "Kindle Store": 9,
    "Patio, Lawn & Garden": 10,
    "Home & Kitchen": 11,
    "CDs & Vinyl": 12,
    "Entertainment Collectibles": 13,
    "Apps & Games": 14,
    "Sports & Outdoors": 15,
    "Clothing, Shoes & Jewelry": 16,
    "Office Products": 17,
    "Computers & Accessories": 18,
    "Amazon Launchpad": 19,
    "Pet Supplies": 20,
    "Movies & TV": 21,
    "Kitchen & Dining": 22,
    "Health & Household": 23,
    "Gift Cards": 24,
    "Electronics": 25,
    "Industrial & Scientific": 26,
    "Magazine Subscriptions": 27,
    "Toys & Games": 28,
    "Amazon Devices & Accessories": 29,
    "Digital Music": 30,
    "Cell Phones & Accessories": 31,
    "Sports Collectibles": 32,
    "Baby": 33,
    "Automotive": 34,
    "Camera & Photo": 35,
    "Video Games": 36}

if __name__ == '__main__':
    cat_arr = set()
    doc_files = os.listdir(data_path)
    for filename in doc_files:
        with open(data_path + filename) as input_file:
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
    for i in range(1, 37):
        out_file_arr.append(open(data_cat_path + str(i), "w"))
    for filename in doc_files:
        with open(data_path + filename) as input_file:
            for line in input_file.readlines():
                obj = json.loads(line.strip())
                cat = obj["cat"]["1"]
                cat_id = cat2id[cat]
                out_file_arr[cat_id - 1].write(line.strip() + "\n")
