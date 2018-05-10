from index import Index


if __name__ == '__main__':

    my_index = Index()

    my_index.read_docs_file()
    my_index.gen_index()
    my_index.write_index_file()
    print("Create index file OK! You can run mysearch.")

# end