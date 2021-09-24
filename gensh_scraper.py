import scrapy

class GenshinSpider(scrapy.Spider):
    name = 'genshinspider'
    start_urls = ['https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN']

    def parse(self, response):
        for article in response.css('div.char_sea_cont'):
            yield{
                'name': article.css('span.sea_charname::text').extract()
            }
        
        
        # for div in response.css('div.char_sea-cont'): 
        #     yield {
        #         'name': div.css('.custom_title::text').extract_first()
        #     }
            

