from index import Index
import pretreatment
import search

if __name__ == '__main__':

    # pretreatment.pre_process()

    my_index = Index()
    my_index.gen_index()
    # my_index.write_index_file()
    # my_index.load_index_file()
    my_index.print_index()
    print("Get index successfully.")

    w1 = "iphon"
    w2 = "silver"
    if my_index.word2id_map[w1] in my_index.index and my_index.word2id_map[w2] in my_index.index:
        result = search.positional_intersect(my_index.index[my_index.word2id_map[w1]], my_index.index[my_index.word2id_map[w2]], 5)
        print(result)