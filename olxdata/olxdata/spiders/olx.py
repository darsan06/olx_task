import scrapy

class olx1(scrapy.Spider):
    name="house"
    start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self,response):
        for products in response.css('li.EIR5N'):
          try:
            yield{
                'name':products.css('span._2tW1I::text').get(),
                'price':products.css('span._89yzn::text').get(),
                'link':products.css('a.fhlkh').attrib['href'],
            }
          except:
               yield{
                'name':products.css('li._2tW1I::text').get(),
                
                
            }
        loadmore = ['https://www.olx.in/api/relevance/v2/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page=1&platform=web-desktop&size=40&user=17f6d5f927dx70e41420']
        if loadmore is not None:
            yield response.follow(loadmore,callback=self.parse)


