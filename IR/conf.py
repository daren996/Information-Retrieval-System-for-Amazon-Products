"""
Configurations

"""

clean_rule = r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt | rt |\n'

stopwords_file = "./stopwords/google_stopwords.txt"

data_ori_path = "./input/data_origin/"
data_path = "./input/doc_data/"

D_path = "./input/index_data/D"
word_set_path = "./input/index_data/word_list"
word2id_map_path = "./input/index_data/word2id_map"
index_path = "./input/index_data/index"

fileid_path = "./input/index_data/fileid.txt"

datafile2id = {"bestseller": 1}  # use this to generate doc_id
magnitude = 100000000
