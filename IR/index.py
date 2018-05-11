"""
The progress of indexing:
    1 Extract one part documents from disk
    2 Map all words to an id
    3 Get all documents belonging to each words and sort them
    4 Combine the sorted results of each part, and finally write them back to disk
"""

import os
import json
import conf
import pickle


class Index:

    def __init__(self):
        self.word_set = set()   # all words
        self.word2id_map = {}   # map : word -> word_id
        self.index = {}         # map & set : word_id -> docs_set
        self.D = 0              # int : The total number of documents
        self.W = 0              # int : The total number of words
        self.doc_files = []     # list of doc files' name

    def get_docs(self):
        pass

    def gen_index(self):
        self.doc_files = os.listdir(conf.data_path)
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
                    text_split = text.split(' ')
                    for w in text_split:
                        if w not in self.word_set:
                            self.W += 1
                            self.word_set.add(w)
                            self.word2id_map[w] = self.W
                        if self.word2id_map[w] not in self.index:
                            self.index[self.word2id_map[w]] = set()
                        self.index[self.word2id_map[w]].add(doc_id)
        # print("The number of documents is %d. \nThe number of words is %d" % (self.D, self.W))

    def write_index_file(self):
        with open(conf.word_set_path, 'wb') as out_file:
            out_file.write(pickle.dumps(self.word_set))
        with open(conf.word2id_map_path, 'wb') as out_file:
            out_file.write(pickle.dumps(self.word2id_map))
        with open(conf.index_path, 'wb') as out_file:
            out_file.write(pickle.dumps(self.index))
        with open(conf.D_path, 'wb') as out_file:
            out_file.write(pickle.dumps(self.D))
        print("Write index to file successfully.")

    def load_index_file(self):
        with open(conf.word_set_path, 'rb') as input_file:
            self.word_set = pickle.loads(input_file.read())
        with open(conf.word2id_map_path, 'rb') as input_file:
            self.word2id_map = pickle.loads(input_file.read())
        with open(conf.index_path, 'rb') as input_file:
            self.index = pickle.loads(input_file.read())
        with open(conf.D_path, 'rb') as input_file:
            self.D = pickle.loads(input_file.read())
        self.W = len(self.word_set)
        print("Load index from file successfully.")

    def print_index(self):
        print("The number of documents is %d. \nThe number of words is %d" % (self.D, self.W))
        for w in self.word_set:
            print("%s\t:\t%s" % (w, self.index[self.word2id_map[w]]))


if __name__ == '__main__':
    my_index = Index()
    my_index.gen_index()
    # my_index.write_index_file()
    # my_index.load_index_file()
    my_index.print_index()
    print("Get index successfully.")
