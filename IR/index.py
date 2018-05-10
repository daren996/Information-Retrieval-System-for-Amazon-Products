import conf
from DocumentSet import DocumentSet


class Index:
    docs = []  # include document name and document content
    doc_id2name = {}
    index = {}

    def __init__(self, data_path, index_path, fileid_path):
        self.data_path = data_path
        self.index_path = index_path
        self.fileid_path = fileid_path
        self.wordList = []
        self.word2id_map = {}
        self.document_set = DocumentSet(self.data_path, self.word2id_map, self.wordList)
        print("Read all files OK")

    def gen_index(self):
        pass

    def write_index_file(self):
        pass


if __name__ == '__main__':
    my_index = Index(conf.data_path, conf.index_path, conf.fileid_path)
    my_index.gen_index()
    my_index.write_index_file()
    print("Create index file OK! You can run Search Program.")
