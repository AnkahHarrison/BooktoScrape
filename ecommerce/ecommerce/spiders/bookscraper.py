import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    base_url="https://books.toscrape.com"

    def parse(self, response):
        for link in response.xpath("//article[@class='product_pod']/h3/a/@href"):
           yield response.follow(link,self.product_parse)
    
    def product_parse(self,response):
        yield{"title":response.xpath("//h1/text()").get(),
              "price": response.xpath("//p[@class='price_color']/text()").get(),
              "rating":response.xpath("//p[contains(@class,'star-rating')]/@class").get(),
              "description": response.xpath("//article[@class= 'product_page']/p").get(),
              "upc":response.xpath("//table//tr[1]/td/text()").get(),
              "Product Type":response.xpath("//table//tr[2]/td/text()").get(),
              "Price (excl. tax)":response.xpath("//table//tr[3]/td/text()").get(),
              "Price (incl. tax)":response.xpath("//table//tr[4]/td/text()").get(),
              "Tax":response.xpath("//table//tr[5]/td/text()").get(),
              "Availability":response.xpath("//table//tr[6]/td/text()").get(),
              "Number of reviews":response.xpath("//table//tr[7]/td/text()").get(),
            
              
              }