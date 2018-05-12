"""
Search program
    1 _p1 and _p2 are indexes of two search terms and k is distance of terms
    2 result is a list contains all result tuples, such as (doc_id, term1_place, term2_place)

@author: Darren
"""


def positional_intersect(_p1, _p2, k):
    result = []
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

