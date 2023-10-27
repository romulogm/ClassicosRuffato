import scrapy
from ..items import RuffatoItem


class LendoclassicosSpider(scrapy.Spider):
    name = "lendoclassicos"
    allowed_domains = ["lendoosclassicosluizruffato.blogspot.com"]
    start_urls = ["http://lendoosclassicosluizruffato.blogspot.com/2021/09/tempestades-de-aco-1920-ernst-junger.html"]

    def parse(self, response):
        print("\n")
        print("HTTP STATUS: "+str(response.status))
        
        blog_archive = response.xpath('//*[@id="BlogArchive1"]')
        links_list = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[2]/div/div[1]/div/ul[1]/li/ul[1]/li/ul/li[3]/a/text()').get()
        title = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/p[1]/span/text()').get()    
        
        pub_year = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p[1]/span[2]/text()').get().replace('(', '').replace(')', '')
        print(blog_archive)
        print(links_list)
        print(title)
        print(pub_year)

        items = RuffatoItem()

        items['title'] = title 
        items['pub_year'] = pub_year

        yield items


    # //blog_archive = response.xpath('//*[@id="BlogArchive1"]')

    #     # Use XPath again to select all <a> elements inside the selected element and extract the href attributes
    #     for link in blog_archive.xpath('.//a'):
    #         href = link.xpath('@href').get()
    #         yield {
    #             'href': href
    #         }