"""
Search program
    1 index_arr is a list contains indexes of several search terms
    2 the result is a list contains all result doc_ids

"""
import math
import operator
import conf
import linecache
import json


class Search:

    def __init__(self, index_arr):
        # list of index: two level map : word_id -> doc_id -> positions i.e. index[word_id][doc_id] = doc_position
        # the definition of doc_position is on util.py
        self.index_arr = index_arr

    # Give 2 keywords and the longest distance k
    def positional_intersect(self, k):
        result = []
        _p1 = self.index_arr[0]
        _p2 = self.index_arr[1]
        p1_iter = iter(sorted(_p1.keys()))  # such as ['01000001', '01000003', '03000001', '03000003', '03000007']
        p2_iter = iter(sorted(_p2.keys()))  # such as ['01000001', '03000001']
        p1 = p1_iter.__next__()
        p2 = p2_iter.__next__()
        while True:
            if p1 == p2:  # if two words both occurrence on the same doc
                pos1 = sorted(list(_p1[p1].pos))
                pos2 = sorted(list(_p2[p2].pos))
                for position1 in pos1:
                    temp = []
                    for position2 in pos2:
                        if abs(position1 - position2) <= k:
                            temp.append(position2)
                        elif position2 > position1:
                            break
                    for t in temp:
                        result.append(p1)
                try:
                    p1 = p1_iter.__next__()
                    p2 = p2_iter.__next__()
                except StopIteration:
                    break
            elif p1 < p2:
                try:
                    p1 = p1_iter.__next__()
                except StopIteration:
                    break
            else:
                try:
                    p2 = p2_iter.__next__()
                except StopIteration:
                    break
        return result

    # Based on tf-idf weighted scores and sorting. some improvement
    # tf = number of occurrences of a word in an article / total number of articles
    # idf = log (the total number of documents in corpus / (number of documents containing the word + 1)
    # D is the number of documents in corpus. k is the number of results returned.
    # doc_length is map : doc_id -> length of this doc.
    def tf_idf_arrange(self, D, k, doc_length):
        word_idf = {}  # word_id -> times or idf value
        doc_score = {}  # doc_id -> score
        doc_cover = {}  # doc_id -> the number of queries covered by each doc
        score_max = 999
        for word_id in range(len(self.index_arr)):
            if word_id not in word_idf:
                word_idf[word_id] = len(self.index_arr[word_id])
        for word_id in word_idf:
            word_idf[word_id] = math.log(D / (word_idf[word_id] + 1))
        print(word_idf)
        for word_id in range(len(self.index_arr)):
            for doc_id in self.index_arr[word_id]:
                if doc_id not in doc_score:
                    doc_score[doc_id] = 0
                if doc_id not in doc_cover:
                    doc_cover[doc_id] = 0
                doc_cover[doc_id] += 1
                doc_score[doc_id] += word_idf[word_id] * (self.index_arr[word_id][doc_id].occur / doc_length[doc_id])
                if doc_score[doc_id] > score_max:
                    score_max = doc_score[doc_id]
        for doc_id in doc_score:
            doc_score[doc_id] += score_max * doc_cover[doc_id]
        doc_sorted = sorted(doc_score.items(), key=operator.itemgetter(1), reverse=True)
        result = [doc[0] for doc in doc_sorted[0:k]]
        return result

    # Query Expansion Algorithm Based on Cluster and Cosine Similarity
    def cluster_extend(self, D, k, doc_length):
        result = self.tf_idf_arrange(D, k, doc_length)
        file_id_arr = {}  # number of extends of each categories
        cat_id_word_set = {}  # word set of each category
        for doc_id in result:
            line = linecache.getline(conf.data_path + conf.id2datafile[str(doc_id)[0]], doc_id % conf.magnitude)
            json_obj = json.loads(line.strip())
            cat = json_obj["cat"]["1"]
            file_id = conf.cat2id[cat]
            if file_id not in file_id_arr:
                file_id_arr[file_id] = 0
            if file_id not in cat_id_word_set:
                cat_id_word_set[file_id] = set()
            text = set(json_obj["name"].split(" "))
            cat_id_word_set[file_id] |= text
            file_id_arr[file_id] += 1
        for f in file_id_arr:
            file_id_arr[f] = int(file_id_arr[f] / len(result) * (k - len(result))) + 1
        new_result = []
        for file_id in file_id_arr:
            count = file_id_arr[file_id]
            doc_id2score = {}
            with open(conf.data_cat_path + str(file_id), "r")as input_file:
                for line in input_file.readlines():
                    json_obj = json.loads(line.strip())
                    doc_id = json_obj["id"]
                    text = set(json_obj["name"].split(" "))
                    if doc_id not in result:
                        doc_id2score[doc_id] = len(text & cat_id_word_set[file_id])
            score_sorted = sorted(doc_id2score.items(), key=operator.itemgetter(1), reverse=True)
            for i in range(min(count, len(score_sorted))):
                new_result.append((score_sorted[i][0], score_sorted[i][1]))
        result_sorted = sorted(new_result, key=operator.itemgetter(1), reverse=True)
        result = result + [r[0] for r in result_sorted]
        return result[0:min(len(result), k)]

    # write your algorithm here
    def other_method(self):
        pass
