import scrapy
import numpy
from amazon.items import AmazonItem


class AmazonSpider(scrapy.Spider):

    name = "Amazon"
    # set delay time 4s
    download_delay = 4
    # the first url
    allowed_domains = ['amazon.com']
    start_urls = [
        # "https://www.amazon.com/Baby-Clothing-Shoes/b/ref=sd_allcat_sft_baby?ie=UTF8&node=7147444011"]
        # "https://www.amazon.com/Mens-Fashion/b/ref=sv_sl_1?ie=UTF8&node=7147441011"]
        # "https://www.amazon.com/Womens-Fashion/b/ref=sv_sl_0?ie=UTF8&node=7147440011"]
        # "https://www.amazon.com/Girls-Fashion/b/ref=sv_sl_2?ie=UTF8&node=7147442011"]
        "https://www.amazon.com/Boys-Fashion/b/ref=sv_sl_3?ie=UTF8&node=7147443011"]
    count = 0

    # def parse4(self, response):
    #     items = response.xpath("//div[@class='zg_itemImmersion']//div[@class='zg_itemWrapper']")
    #     try:
    #         cat = {1: response.xpath("//div[@id='zg_left_col2']//ul[@id='zg_browseRoot']//ul/li["
    #                                  "@class='zg_browseUp']/a/text()").extract()[0].strip(),
    #                2: response.xpath("//div[@id='zg_left_col2']//ul//ul//span[@class='zg_selected']/"
    #                                  "text()").extract()[0].strip()}
    #     except:
    #         cat = {1: None, 2: None}
    #         with open("result/error.txt", "a") as outfile:
    #             outfile.write("error: " + response)
    #     for i in items:
    #         item = AmazonItem()
    #         item['url'] = "https://www.amazon.com" + i.xpath(".//a[@class='a-link-normal']/@href").extract()[0]
    #         item['name'] = i.xpath(".//a[@class='a-link-normal']//div[2]/text()").extract()[0].strip()
    #         item['cat'] = cat
    #         yield item

    def parse5(self, response):
        print('test5')
        title = response.xpath("//span[@id='productTitle']/text()").extract()[0].strip()
        cat = response.xpath("//a[@class='a-link-normal a-color-tertiary']/text()").extract()
        price = response.xpath("//span[@id='priceblock_ourprice']/text()").extract()[0].strip()
        star = response.xpath("//div[@id='averageCustomerReviews']//span[@class='a-icon-alt']/text()").extract()
        description = response.xpath("//*[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()
        product_description = response.xpath("//*[@id='productDescription']/p/text()").extract()
        details = response.xpath("//*[@id='detailBullets_feature_div']/ul/li/span[@class='a-list-item']/span[@class='a-text-bold']/text()").extract()
        details1 = response.xpath("//*[@id='detailBullets_feature_div']/ul/li/span[@class='a-list-item']/span").extract()
        #//*[@id="landingImage"]//*[@id="landingImage"]//*[@id="imgTagWrapperId"]
        picture = response.xpath("//div[@class='imgTagWrapper']/img/@data-a-dynamic-image").extract()

        item = AmazonItem()
        item['title'] = title
        item['cat'] = cat
        item['price'] = price
        item['star'] = star
        item['url'] = response.url
        item['description'] = description
        item['Product_description'] = product_description
        item['details'] = details
        item['details1'] = details1
        item['picture'] = picture
        yield item

    def parse4(self, response):  # casual
        print('test4')

        urls = response.xpath("//a[@class ='a-link-normal s-access-detail-page s-overflow-ellipsis s-color-twister-title-link a-text-normal']/@href").extract()
        for u in urls:
            print(u)
            yield scrapy.Request(u, dont_filter=True, callback=self.parse5)
        next_page = response.xpath("//a[@id='pagnNextLink']/@href").extract()
        print("next page!", next_page)
        if len(next_page) > 0:
            yield scrapy.Request("https://www.amazon.com"+next_page[0], dont_filter=True, callback=self.parse4)
        pass

    def parse3(self, response):#casual
        print('test3')
# //*[@id="leftNav"]/ul[1]/ul/li/span/ul/div/li[2]/span/ul/div/li[2]/span/a/span
        urls = response.xpath("// ul / ul / li / span / ul / div // li/ span / ul / div // li / span / ul / div // li / span // a[@class ='a-link-normal s-ref-text-link']/@href").extract()
        # urls = response.xpath("//*[@id='leftNav']/ul[1]/ul/li/span/ul/div/li[2]/span/ul/div/li[2]/span//a/@href").extract()
        print("test3**", urls)
        for u in urls:
            print("********", response.xpath("// ul / ul / li / span / ul / div // li/ span / ul / div // li / span / ul / div // li / span // a[@class ='a-link-normal s-ref-text-link']/span/text()").extract())
            url = "https://www.amazon.com" + u
            yield scrapy.Request(url, dont_filter=True, callback=self.parse4)
            # break
        pass

    def parse2(self, response):  # dresses
        print('test2')
        urls = response.xpath("//ul[@class='a-unordered-list a-nostyle a-vertical s-ref-indent-one']//a[@class ='a-link-normal s-ref-text-link']/@href").extract()
        for u in urls:
            url="https://www.amazon.com"+u
            yield scrapy.Request(url, dont_filter=True, callback=self.parse3)
            # break
        pass

    def parse(self, response):  # clothing
        print('test1')

        urls = response.xpath(" // ul // li //a[@class='a-link-normal s-ref-text-link']/@href").extract()
        # yield scrapy.Request(urls[0], callback=self.parse2)
        for u in urls:
            url = "https://www.amazon.com" + u
            print(url)
            yield scrapy.Request(url, dont_filter=True, callback=self.parse2)
            # break
        pass
