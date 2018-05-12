"""
The progress of indexing:
    1 Extract one part documents from disk
    2 Map all words to an id
    3 Get all documents belonging to each words and sort them
    4 Get positional information
    5 Combine the sorted results of each part, and finally write them back to disk

@author: Darren
"""

import os
import json
import conf
import pickle
import util
from util import doc_position


class Index:

    def __init__(self):
        self.word_set = set()  # all words
        self.word2id_map = {}  # map : word -> word_id
        self.index = {}  # map & set : word_id -> doc_id -> positions  index[word_id][doc_id] = doc_position
        self.D = 0  # int : The total number of documents
        self.W = 0  # int : The total number of words
        self.doc_files = []  # list of doc files' name

    def get_docs(self):
        pass

    def gen_index(self, file_name=None):
        if file_name:
            self.doc_files = [file_name]
        else:
            self.doc_files = os.listdir(conf.data_path)
        print("List of document files: ", self.doc_files)
        for filename in self.doc_files:
            with open(conf.data_path + filename) as input_file:
                for line in input_file.readlines():
                    self.D += 1
                    try:
                        obj = json.loads(line.strip())
                    except json.decoder.JSONDecodeError:
                        print("****JSONDecodeError on line: \n****", line)
                        exit(-1)
                    text = obj['name']  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    doc_id = obj['id']
                    pos = 0
                    text_split = text.split(' ')
                    for w in text_split:
                        pos += 1
                        if w not in self.word_set:
                            self.W += 1
                            self.word_set.add(w)
                            self.word2id_map[w] = self.W
                        if self.word2id_map[w] not in self.index:
                            self.index[self.word2id_map[w]] = {}
                        if doc_id not in self.index[self.word2id_map[w]]:
                            self.index[self.word2id_map[w]][doc_id] = doc_position(doc_id)  # positional index
                        self.index[self.word2id_map[w]][doc_id].insert(pos)
        # print("The number of documents is %d. \nThe number of words is %d" % (self.D, self.W))

    def write_index_file(self):
        with open(conf.word_set_path + ".decompress", 'wb') as out_file:
            out_file.write(pickle.dumps(self.word_set))
        with open(conf.word2id_map_path + ".decompress", 'wb') as out_file:
            out_file.write(pickle.dumps(self.word2id_map))
        with open(conf.index_path + ".decompress", 'wb') as out_file:
            out_file.write(pickle.dumps(self.index))
        with open(conf.D_path + ".decompress", 'wb') as out_file:
            out_file.write(pickle.dumps(self.D))
        util.compress(conf.word_set_path + ".decompress", conf.word_set_path)
        util.compress(conf.word2id_map_path + ".decompress", conf.word2id_map_path)
        util.compress(conf.index_path + ".decompress", conf.index_path)
        util.compress(conf.D_path + ".decompress", conf.D_path)
        os.remove(conf.word_set_path + ".decompress")
        os.remove(conf.word2id_map_path + ".decompress")
        os.remove(conf.index_path + ".decompress")
        os.remove(conf.D_path + ".decompress")
        print("Write index to file successfully.")

    def load_index_file(self):
        util.decompress(conf.word_set_path, conf.word_set_path + ".decompress")
        util.decompress(conf.word2id_map_path, conf.word2id_map_path + ".decompress")
        util.decompress(conf.index_path, conf.index_path + ".decompress")
        util.decompress(conf.D_path, conf.D_path + ".decompress")
        with open(conf.word_set_path + ".decompress", 'rb') as input_file:
            self.word_set = pickle.loads(input_file.read())
        with open(conf.word2id_map_path + ".decompress", 'rb') as input_file:
            self.word2id_map = pickle.loads(input_file.read())
        with open(conf.index_path + ".decompress", 'rb') as input_file:
            self.index = pickle.loads(input_file.read())
        with open(conf.D_path + ".decompress", 'rb') as input_file:
            self.D = pickle.loads(input_file.read())
        self.W = len(self.word_set)
        os.remove(conf.word_set_path + ".decompress")
        os.remove(conf.word2id_map_path + ".decompress")
        os.remove(conf.index_path + ".decompress")
        os.remove(conf.D_path + ".decompress")
        print("Load index from file successfully.")

    def print_index(self):
        print("The number of documents is %d. \nThe number of words is %d" % (self.D, self.W))
        for w in self.word_set:
            print(w, ":", end="")
            for doc_id in self.index[self.word2id_map[w]]:
                doc_pos = self.index[self.word2id_map[w]][doc_id]
                print("\t", doc_id, ", ", doc_pos.occur, ": ", doc_pos.pos, end="")
            print()


if __name__ == '__main__':
    my_index = Index()
    # my_index.gen_index()
    # my_index.write_index_file()
    my_index.load_index_file()
    my_index.print_index()
    print("Get index successfully.")
