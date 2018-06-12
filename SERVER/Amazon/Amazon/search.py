# -*- coding: utf-8 -*-

import sys
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from Database.models import Product
from Database.models import User_1
from Database.models import UserProd
import nltk
import re
import IR.conf
import IR.corrector
from IR.index import Index
from IR.search import Search
from nltk.corpus import wordnet as wn


def register(request):
    return render_to_response('register.html')


log_in = False
log_num = 0


def recommend():
    if log_in:
        set_recommended = getItem(log_num)
        NumUser = User_1.objects.all()
        max = 0
        BestLikeEmail = 0
        set_cha = []
        for i in range(0, len(NumUser)):
            if NumUser[i].Email != log_num:
                set_other = getItem(NumUser[i].Email)
                set_Inter = [val for val in set_recommended if val in set_other]
                set_Union = list(set(set_recommended).union(set(set_other)))

                if len(set_Union) != 0:
                    if len(set_Inter) / len(set_Union) > max:
                        max = len(set_Inter) / len(set_Union)
                        BestLikeEmail = NumUser[i].Email
                        set_cha = list(set(set_other).difference(set(set_recommended)))
        return set_cha


def getItem(a):
    userprod = UserProd.objects.filter(Email=a)
    new_object = []
    for i in range(0, len(userprod)):
        new_object.append(userprod[i].Item)
    return new_object


def search_function(search_words, fun="cluster"):
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
        return -2
    search_obj = Search(index_arr)
    if fun == "cluster":
        result = search_obj.cluster_extend(my_index.D, 40, my_index.doc_length)  # change search algorithm here
    elif fun == "star":
        result = search_obj.star_arrange(my_index.D, 40, my_index.doc_length)
    # elif fun == "category":
    #     result = search_obj.cluster_extend(my_index.D, 40, my_index.doc_length)
    # elif fun == "recommend":
    #     result = search_obj.cluster_extend(my_index.D, 40, my_index.doc_length)
    return result


def addUser(request):
    global i
    global log_in
    global log_num
    Sex = request.GET['Sex']
    first_name_1 = request.GET['first_name_1']
    last_name_1 = request.GET['last_name_1']
    Email = request.GET['Email']
    Password = request.GET['Password']
    Years = request.GET['Years']
    Month = request.GET['Month']
    days = request.GET['days']
    first_name_2 = request.GET['first_name_2']
    last_name_2 = request.GET['last_name_2']
    company = request.GET['company']
    Adress = request.GET['Adress']
    Adress_line_2 = request.GET['Adress_line_2']
    city = request.GET['city']
    state = request.GET['state']
    Zip = request.GET['Zip']
    country = request.GET['company']
    aditionalInfo = request.GET['aditionalInfo']
    phone = request.GET['phone']
    mobile = request.GET['mobile']
    user = User_1(Sex=Sex,
                  first_name_1=first_name_1,
                  last_name_1=last_name_1,
                  Email=Email,
                  Password=Password,
                  Years=Years,
                  Month=Month,
                  days=days,
                  first_name_2=first_name_2,
                  last_name_2=last_name_2,
                  company=company,
                  Adress=Adress,
                  Adress_line_2=Adress_line_2,
                  city=city,
                  state=state,
                  Zip=Zip,
                  country=country,
                  aditionalInfo=aditionalInfo,
                  phone=phone,
                  mobile=mobile)
    log_in = True
    log_num = user.Email
    user.save()
    ctx = {"holder": "You can buy whatever you want through this site!"}
    return render_to_response('index.html', ctx)


def search_history(request):
    global log_in
    global log_num
    ctx = {}
    if log_in:
        ctx['rlt'] = log_num
        request.encoding = 'utf-8'
        ctx["history"] = []
        userprod = UserProd.objects.filter(Email=log_num)
        for r in range(0, min(9, len(userprod))):
            ctx["history"].append(userprod[r].Item)
    else:
        ctx['rlt'] = "You are not logged in yet!"
        ctx = {"holder": "You are not logged in yet!"}
        return render(request, 'notLogin.html', ctx)

    ctx["product5"] = []
    result3_word = recommend()
    if search_function(result3_word, "star") == -2:
        result3 = []
    else:
        result3 = search_function(result3_word, "star")
    for r in result3[0:3]:
        ctx["product5"].append(get_dic(r))
    return render(request, 'UserPage.html', ctx)


def search_form(request):
    ctx = {"holder": "You can buy whatever you want through this site!"}
    return render_to_response('index.html', ctx)


def get_dic(r):
    product = Product.objects.get(P_id=r)
    new_obj = {"title": product.title, "url": product.url}
    if product.price is not None:
        new_obj["price"] = product.price
    else:
        new_obj["price"] = "Price Not Known"
    if product.photo is not None:
        new_obj["photo"] = product.photo
    else:
        new_obj["photo"] = "https://raw.githubusercontent.com/daren996/Information-Retrieval-" \
                           "System-for-Amazon-Products/master/no_image.png"
    return new_obj


def login(request):
    global log_in
    global log_num
    log_in = True
    user = User_1.objects.filter(Email=request.GET['Email'])
    if len(user) == 0:
        ctx = {"holder": "This email has not been registered!"}
        return render_to_response('notLogin.html', ctx)
    elif user[0].Password != request.GET['Password']:
        ctx = {"holder": "Your password is wrong!"}
        return render_to_response('notLogin.html', ctx)
    log_num = user[0].Email
    ctx = {"holder": "You can buy whatever you want through this site!"}
    return render_to_response('index.html', ctx)


def search(request):
    ctx = {}
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        if log_in:
            IsDinstin = False
            userprod_1 = UserProd.objects.filter(Email=log_num)
            ctx['rlt'] = log_num
            if len(userprod_1) == 0:
                userprod = UserProd(Email=log_num, Item=request.GET['q'])
                userprod.save()
            else:
                for i in range(0, len(userprod_1)):
                    if userprod_1[i].Item != request.GET['q']:
                        continue
                    else:
                        IsDinstin = True
                        break

                if not IsDinstin:
                    userprod = UserProd(Email=log_num, Item=request.GET['q'])
                    userprod.save()
        else:
            ctx['rlt'] = "You are not logged in yet!"
        ctx['qlt'] = '你搜索的内容为: ' + request.GET['q']
        search_words_ori = request.GET['q'].split(" ")
        search_words = [IR.corrector.correction(word) for word in search_words_ori]  # corrector for word
        is_corrected = False
        for i in range(len(search_words)):
            if search_words_ori[i] != search_words[i]:
                is_corrected = True
        if is_corrected:
            ctx["correction"] = "Your Search is " + " ".join(search_words_ori) + \
                                ".  Do you mean: " + " ".join(search_words) + "?"
        else:
            ctx["correction"] = ""
        if search_function(search_words, "star") == -2:
            return render_to_response('index.html', {"holder": "Can't get anything. Please search again."})
        result1 = search_function(search_words, "star")
        ctx["product0"] = []
        ctx["product1"] = []
        ctx["product2"] = []
        ctx["product3"] = []
        ctx["product4"] = []
        ctx["product5"] = []
        for r in result1[0:6]:
            ctx["product0"].append(get_dic(r))
        result2 = result1[6:]
        for r in result2[0:4]:
            ctx["product1"].append(get_dic(r))
        for r in result2[4:8]:
            ctx["product2"].append(get_dic(r))
        for r in result2[8:12]:
            ctx["product3"].append(get_dic(r))
        for r in result2[12:16]:
            ctx["product4"].append(get_dic(r))

        search_words2 = []
        for w in search_words_ori:
            w1 = wn.synsets(w)
            for w3 in w1:
                for w2 in w3.lemma_names():
                    search_words2.append(w2)
        if len(search_words2) > len(search_words):
            search_words2 = list(set(search_words2) - set(search_words))
        print(search_words_ori, search_words2)
        search_words_recommend = [IR.corrector.correction(word) for word in search_words2]  # corrector for word
        result3 = search_function(search_words_recommend, "star")
        if result3 != -2:
            for r in result3[0:3]:
                ctx["product5"].append(get_dic(r))
        else:
            for r in result2[16:19]:
                ctx["product5"].append(get_dic(r))
    else:
        ctx['qlt'] = '你提交了空表单'
    return render(request, 'search_result.html', ctx)
