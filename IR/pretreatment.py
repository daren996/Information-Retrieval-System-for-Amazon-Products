"""
The progress of pretreatment:
    1 Remove special symbols
    2 Remove stop words
    3 Extract stem
    4 Remove single-character word

@author: Darren
"""

import os
import json
import nltk
import re
import conf


def read_stopwords():
    with open(conf.stopwords_file, 'r') as fin:
        line = fin.readline()
        line = line.strip()
        stopwords = line.split(' ')
    return stopwords


def process(text, stemmer, stopwords):
    new_text = (re.sub(conf.clean_rule, " ", text))
    words = [stemmer.stem(word) for word in new_text.split()
             if word not in stopwords and len(word) > 1]
    words_no_stop = [word.lower() for word in words if word.lower() not in stopwords]
    new_text = ' '.join(words_no_stop)
    return new_text


def pre_process():
    input_path = conf.data_ori_path
    output_path = conf.data_path
    name_list = os.listdir(input_path)
    print("File name list: ", name_list)
    stemmer = nltk.stem.PorterStemmer()
    stopwords = read_stopwords()
    counter = 0
    for file_name in name_list:
        file_in = open(input_path + file_name, 'r')
        file_out = open(output_path + file_name, 'w')
        for line in file_in:
            json_obj = json.loads(line.strip())
            temp_text = process(json_obj['name'], stemmer, stopwords)
            if temp_text:
                json_obj['name_ori'] = json_obj['name']
                json_obj['name'] = temp_text
            else:
                continue
            json_str = json.dumps(json_obj)
            file_out.write(json_str + '\n')
        file_in.close()
        file_out.close()
        counter += 1
        if counter % 10 == 0:
            print("Processed the %dth file." % counter)


if __name__ == '__main__':
    pre_process()
