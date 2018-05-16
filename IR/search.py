"""
Search program
    1 _p1 and _p2 are indexes of two search terms and k is distance of terms
    2 result is a list contains all result tuples, such as (doc_id, term1_place, term2_place)

"""


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
                        result.append((p1, position1, t))
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

    # write your algorithm here
    def other_method(self):
        pass
