import json
from Document import Document


class DocumentSet:

    def __init__(self, data_path, word2id_map, word_list):
        self.D = 0  # The total number of documents
        self.documents = []
        with open(data_path) as input_file:
            line = input_file.readline()
            while line:
                self.D += 1
                obj = json.loads(line)
                text = obj['textCleaned']
                document = Document(text, word2id_map, word_list, int(obj['tweetId']))
                self.documents.append(document)
                line = input_file.readline()
        print("number of documents is ", self.D)
