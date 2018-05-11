import os
import json
import numpy as np
import nltk
import re
import conf


def process(str, stemmer):
    str_list = str.strip().split(' ')
    list_l = []
    for word in str_list:
        if not word:
            continue
        if word[0] == '#':
            word = word[1:]
        Is_num = re.search(r'[0-9#]', word)
        if Is_num:
            continue
        word = word.lower()
        if word in nltk.corpus.stopwords.words('english'):
            continue
        word = stemmer.stem(word)
        if word:
            list_l.append(word)
    if not list_l:
        if type(str) == str:
            return ''
        else:
            return []
    return ' '.join(list_l)


def tag_proess(tags, stemmer):
    str_list = tags
    list_l = []
    for word in str_list:
        if word[0] == '#':
            word = word[1:]
        Is_num = re.search(r'[0-9#]', word)
        if Is_num:
            continue
        word = word.lower()
        if word in nltk.corpus.stopwords.words('english'):
            continue
        word = stemmer.stem(word)
        if word:
            list_l.append(word)
    if not list_l:
        if type(str) == str:
            return ''
        else:
            return []
    return list_l


def pre_process():
    input_path = conf.data_path
    output_path = conf.data_path
    name_list = os.listdir(input_path)
    stemmer = nltk.stem.PorterStemmer()
    counter = 0
    for file_name in name_list:
        file_in = open(input_path + file_name, 'r')
        file_out = open(output_path + file_name, 'w')
        for line in file_in:
            json_obj = json.loads(line.strip())
            temp_text = process(json_obj['text'], stemmer)
            if temp_text:
                json_obj['text'] = temp_text
            else:
                continue
            temp_tags = tag_proess(json_obj['hashtags'], stemmer)
            if temp_tags:
                json_obj['hashtags'] = temp_tags
            else:
                continue
            json_str = json.dumps(json_obj)
            file_out.write(json_str + '\n')
        file_in.close()
        file_out.close()
        counter += 1
        if counter % 10 == 0:
            print(counter)


if __name__ == '__main__':
    pre_process()
