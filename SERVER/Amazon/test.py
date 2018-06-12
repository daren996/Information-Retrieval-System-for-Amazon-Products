from IR.index import Index
from IR.search import Search
import nltk
import re
import IR.conf
import linecache
import json
from nltk.corpus import wordnet as wn


def syn(word, lch_threshold=2.26):
    # print(wn.synsets(word))
    for net1 in wn.synsets(word):
        j = 0
        for net2 in wn.all_synsets():
            if (j > 5):
                break
            try:
                lch = net1.lch_similarity(net2)
                j = j + 1
            except:
                continue
            # The value to compare the LCH to was found empirically.
            # (The value is very application dependent. Experiment!)
            if lch >= lch_threshold:
                yield (net1, net2, lch)


if __name__ == '__main__':
    my_index = Index()
    my_index.gen_index()
    my_index.write_index_file()
    my_index.load_index_file()
    # my_index.print_index()
    print("Get index successfully.")

    search_word = ["lip"]
    print("search: ", search_word)
    stemmer = nltk.stem.PorterStemmer()
    search_word = [stemmer.stem(re.sub(IR.conf.clean_rule, "", w)) for w in search_word]
    result = []
    index_arr = []
    for w in search_word:
        if w not in my_index.word2id_map or my_index.word2id_map[w] not in my_index.index:
            print("There is no word:", w)
        else:
            index_arr.append(my_index.index[my_index.word2id_map[w]])

    # 同义词
    search_words2 = []
    for w in search_word:
        w1 = wn.synsets(w)
        for w3 in w1:
            for w2 in w3.lemma_names():
                search_words2.append(w2)
    if len(search_words2) > len(search_word):
        search_words2 = list(set(search_words2) - set(search_word))
    print(search_words2)


    if len(index_arr) == 0:
        print("No query word exists!")
        exit(-2)
    search = Search(index_arr)
    # result = search.cluster_extend(my_index.D, 40, my_index.doc_length)  # change search algorithm here
    result = search.star_arrange(my_index.D, 40, my_index.doc_length)
    print(result)

    count = 0
    for doc_id in result:
        line = linecache.getline(IR.conf.data_path + IR.conf.id2datafile[str(doc_id)[0]], doc_id % IR.conf.magnitude)
        json_obj = json.loads(line.strip())
        count += 1
        print(count, doc_id, json_obj["name_ori"])
