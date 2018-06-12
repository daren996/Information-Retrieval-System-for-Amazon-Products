"""
generate id for every doc

"""

import os
import json
import conf

# generate id for every doc
dir_path = "./doc_data/"
# dir_path = "./data_origin/"
doc_files = os.listdir(dir_path)
doc_files.remove("bestseller")
doc_files.remove("ClothingShoesJewelry")
print(doc_files)
for filename in doc_files:
    D = 0
    out_file = open(dir_path + filename+"_new", "w")
    with open(dir_path + filename, "r") as input_file:
        for line in input_file.readlines():
            D += 1
            new_id = D + conf.magnitude * conf.datafile2id[filename]
            json_obj = json.loads(line.strip())
            json_obj['id'] = new_id
            out_file.write(json.dumps(json_obj) + "\n")
    out_file.close()
    os.remove(dir_path + filename)
    os.renames(dir_path + filename+"_new", dir_path + filename)
