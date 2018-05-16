from index import Index
import pretreatment
from search import Search
import nltk
import re
import conf
import linecache
import json

if __name__ == '__main__':

    # pretreatment.pre_process()

    my_index = Index()
    # my_index.gen_index()
    # my_index.write_index_file()
    my_index.load_index_file()
    print("Get index successfully.")

    search_word = ["apple", "tv"]
    print("search: ", search_word)
    stemmer = nltk.stem.PorterStemmer()
    search_word = [stemmer.stem(re.sub(conf.clean_rule, "", w)) for w in search_word]
    result = []
    for w in search_word:
        if w not in my_index.word2id_map:
            print("There is no word:", w)
            exit(-2)
        if my_index.word2id_map[w] not in my_index.index:
            print("There is no word:", w)
            exit(-2)
    index_arr = [my_index.index[my_index.word2id_map[w]] for w in search_word]
    search = Search(index_arr)
    result = search.positional_intersect(5)  # change search algorithm here

    result_doc_id2amount = {}
    for r in result:
        doc_id = r[0]
        if doc_id not in result_doc_id2amount:
            result_doc_id2amount[doc_id] = 0
        result_doc_id2amount[doc_id] += 1
    print(len(result_doc_id2amount), "results")
    for doc_id in result_doc_id2amount:
        line = linecache.getline(conf.data_path + "bestseller", doc_id % conf.magnitude)
        json_obj = json.loads(line.strip())
        print(doc_id, json_obj["name_ori"])
