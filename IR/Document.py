class Document:

    def __init__(self, text, word2id_map, word_list, document_id):
        self.document_id = document_id
        self.wordIdArray = []
        self.wordFreArray = []
        V = len(word2id_map)
        wordFreMap = {}
        ws = text.strip().split(' ')
        for w in ws:
            if w not in word2id_map:
                V += 1
                wId = V
                word2id_map[w] = V
                word_list.append(w)
            else:
                wId = word2id_map[w]

            if wId not in wordFreMap:
                wordFreMap[wId] = 1
            else:
                wordFreMap[wId] = wordFreMap[wId] + 1
                # wordFreMap[wId] = 1
        self.wordNum = wordFreMap.__len__()
        w = 0
        for wfm in wordFreMap:
            self.wordIdArray.append(wfm)
            self.wordFreArray.append(wordFreMap[wfm])
            w += 1