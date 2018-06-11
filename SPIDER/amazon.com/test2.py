import json
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.36 "
}

if __name__ == '__main__':

    pro_id = 300000000
    url_arr = set()
    out_file = open("walmart", "a")
    start_url = "https://www.walmart.com/browse/summersavings-fy19-rbk-globalshelf/0/0/?_be_shelf_id=54991" \
                "&_refineresult=true&facet=shelf_id%3A54991&page=1&search_sort=100#searchProductResult "
    response = requests.get(start_url, headers=headers)
    response.encoding = 'UTF-8'
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    item_arr = soup.find_all('div', class_="search-result-gridview-item-wrapper arrange")
    print("length of item_arr: ", len(item_arr))
    for item in item_arr:
        obj = {}
        name = item.find('a', class_="product-title-link line-clamp line-clamp-2").find_all('span')[0].get_text()
        url = "https://www.walmart.com" + item.find_all('a', class_="product-title-link line-clamp line-clamp-2")[0]. \
            get('href')
        if url in url_arr:
            print("url:", url)
            continue
        else:
            url_arr.add(url)
        # pro_response = requests.get(url, headers=headers)
        # pro_response.encoding = 'UTF-8'
        # pro_page = pro_response.text
        # pro_soup = BeautifulSoup(pro_page, 'html.parser')
        # cat1 = pro_soup.find_all('ol', class_='breadcrumb-list ')[0].find_all('a')[0].get_text()
        # cat2 = pro_soup.find_all('ol', class_='breadcrumb-list ')[0].find_all('a')[1].get_text()
        cat = {}
        price = item.find_all('span', class_="price-characteristic")
        picture_arr = item.find('div', class_="display-inline-block pull-left prod-ProductCard--Image").find_all('img')
        star = item.find('div', class_="stars stars-small").find('span', class_='seo-avg-rating')
        pro_id += 1
        obj["name"] = name
        obj["url"] = url
        obj["cat"] = cat
        obj["price"] = "$" + price[0].get_text()
        obj["picture"] = [picture_arr[0].get('src')]
        obj["star"] = str(star.get_text()) + " out of 5 stars"
        obj["id"] = pro_id
        print(obj)
    item_arr = soup.find_all('div', class_="search-result-gridview-item-wrapper arrange")
    print("length of item_arr: ", len(item_arr))
    for item in item_arr:
        obj = {}
        name = item.find('a', class_="product-title-link line-clamp line-clamp-2").find_all('span')[0].get_text()
        url = "https://www.walmart.com" + item.find_all('a', class_="product-title-link line-clamp line-clamp-2")[0]. \
            get('href')
        if url in url_arr:
            print("url:", url)
            continue
        else:
            url_arr.add(url)
        # pro_response = requests.get(url, headers=headers)
        # pro_response.encoding = 'UTF-8'
        # pro_page = pro_response.text
        # pro_soup = BeautifulSoup(pro_page, 'html.parser')
        # cat1 = pro_soup.find_all('ol', class_='breadcrumb-list ')[0].find_all('a')[0].get_text()
        # cat2 = pro_soup.find_all('ol', class_='breadcrumb-list ')[0].find_all('a')[1].get_text()
        cat = {}
        price = item.find_all('span', class_="price-characteristic")
        picture_arr = item.find('div', class_="display-inline-block pull-left prod-ProductCard--Image").find_all('img')
        star = item.find('div', class_="stars stars-small").find('span', class_='seo-avg-rating')
        pro_id += 1
        obj["name"] = name
        obj["url"] = url
        obj["cat"] = cat
        obj["price"] = "$" + price[0].get_text()
        obj["picture"] = [picture_arr[0].get('src')]
        obj["star"] = str(star.get_text()) + " out of 5 stars"
        obj["id"] = pro_id
        print(obj)
