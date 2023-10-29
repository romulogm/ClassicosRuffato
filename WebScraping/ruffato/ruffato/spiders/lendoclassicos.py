import scrapy
from ..items import RuffatoItem
from ruffato.data.html_remover import replace_between_angle_brackets 
import json


class LendoclassicosSpider(scrapy.Spider):
    name = "lendoclassicos"
    allowed_domains = ["lendoosclassicosluizruffato.blogspot.com"]
    # start_urls = ["http://lendoosclassicosluizruffato.blogspot.com/2021/09/o-livro-do-xadrez-1942-stefan-zweig.html",
                #   "http://lendoosclassicosluizruffato.blogspot.com/2021/11/o-mundo-se-despedaca-1958-chinua-achebe.html",
                #   "http://lendoosclassicosluizruffato.blogspot.com/2015/12/a-ultima-nevoa-1935-maria-luisa-bombal.html"]
    with open(r"C:\Users\romul\OneDrive\Documentos\CS\ClassicosRuffato\WebScraping\ruffato\ruffato\data\links_list.json", 'r') as json_file:
        start_urls = json.load(json_file)
        
    def parse(self, response):
        print("HTTP STATUS: "+str(response.status))                
        post_content = response.css('div[id*=post-body-]').get()
        cleaned_content = replace_between_angle_brackets(post_content)
        
        items = RuffatoItem()
        items['post_content'] = cleaned_content
        items['url'] = response.request.url
        yield items

