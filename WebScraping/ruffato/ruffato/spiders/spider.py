import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["http://lendoosclassicosluizruffato.blogspot.com/2021/09/tempestades-de-aco-1920-ernst-junger.html"]

    def parse(self, response):
        # Use XPath to select the element with id="BlogArchive1"
        blog_archive = response.xpath('//*[@id="BlogArchive1"]')

        # Use XPath again to select all <a> elements inside the selected element and extract the href attributes
        for link in blog_archive.xpath('.//a'):
            href = link.xpath('@href').get()
            yield {
                'href': href
            }