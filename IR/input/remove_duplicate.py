"""
remove duplicate

"""

import os
import json

# remove duplicate
# dir_path = "./doc_data/"
dir_path = "./data_origin/"
url_set = set()
doc_files = os.listdir(dir_path)
print(doc_files)
for filename in doc_files:
    out_file = open(dir_path + filename+"_new", "w")
    with open(dir_path + filename, "r") as input_file:
        for line in input_file.readlines():
            json_obj = json.loads(line.strip())
            url = json_obj['url']
            if url not in url_set:
                url_set.add(url)
                out_file.write(json.dumps(json_obj) + "\n")
    out_file.close()
    # os.remove(dir_path + filename)
    # os.renames(dir_path + filename+"_new", dir_path + filename)
