# -*- coding: utf-8 -*-

import sys
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from Database.models import Product
import nltk
import re
import IR.conf
from IR.index import Index
from IR.search import Search


def search_function(search_words):
    my_index = Index()
    # my_index.gen_index()
    # my_index.write_index_file()
    my_index.load_index_file()
    print("Get index successfully.")

    print("search: ", search_words)
    stemmer = nltk.stem.PorterStemmer()
    search_words = [stemmer.stem(re.sub(IR.conf.clean_rule, "", w)) for w in search_words]
    result = []
    index_arr = []
    for w in search_words:
        if w not in my_index.word2id_map or my_index.word2id_map[w] not in my_index.index:
            print("There is no word:", w)
        else:
            index_arr.append(my_index.index[my_index.word2id_map[w]])
    if len(index_arr) == 0:
        print("No query word exists!")
        exit(-2)
    search = Search(index_arr)
    result = search.cluster_extend(my_index.D, 40, my_index.doc_length)  # change search algorithm here
    return result


def search_form(request):
    return render_to_response('index.html')


def search(request):
    ctx = {}
    request.encoding = 'utf-8'
    # ctx['id'] = Product.objects.all()[0].P_id
    if 'q' in request.GET:
        ctx['rlt'] = '你搜索的内容为: ' + request.GET['q']
        search_words = request.GET['q'].split(" ")
        result = search_function(search_words)
        ctx["product"] = []
        for r in result[0:10]:
            product = Product.objects.get(P_id=r)
            ctx["product"].append({"title": product.title, "url": product.url})
    else:
        ctx['rlt'] = '你提交了空表单'
    return render(request, 'search_result.html', ctx)
