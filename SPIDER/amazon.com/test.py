import json
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.36 "
}


if __name__ == '__main__':

    pro_id = 100013305
    out_file = open("bestseller_new", "a")
    with open("bestseller", "r") as in_file:
        for line in in_file.readlines():
            obj = json.loads(line.strip())
            if obj["id"] < pro_id:
                continue
            url = obj["url"]
            response = requests.get(url, headers=headers)
            response.encoding = 'UTF-8'
            page = response.text
            soup = BeautifulSoup(page, 'html.parser')
            try:
                imgList = soup.find('div', id="imgTagWrapperId").find_all('img')
                obj["picture"] = [src[0] for src in json.loads(imgList[0].get('data-a-dynamic-image')).items()]
            except:
                print("photo", obj["id"], url)
            try:
                price = soup.find('span', id='priceblock_ourprice')
                obj["price"] = price.string
            except:
                print("price", obj["id"], url)
            try:
                star = soup.find('span', id='acrPopover').find('span', class_='a-declarative'). \
                    find('span', class_='a-icon-alt')
                obj["star"] = star.string
            except:
                print("star", obj["id"], url)
            out_file.write(json.dumps(obj) + "\n")


