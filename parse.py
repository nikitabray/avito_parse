import requests
from bs4 import BeautifulSoup

class GetUrl():
    def __init__(self, *args, **kwargs):
        self.url = input("Введите url категории: ")

    def get_url(self):
        if self.url:
            return self.url
        else:
            return 'https://www.avito.ru/moskva/telefony/mobile/apple-ASgBAgICAkS0wA3OqzmwwQ2I_Dc'

class GetDocument():
    def __init__(self, url=None, *args, **kwargs):
        self.url = url

    def get_document(self):
        return requests.get(self.url).text

class ToTheParse():
    def __init__(self, document=None, parser='html.parser', *args, **kwargs):
        self.document = document
        self.parser = parser

    def get_product_title_and_price(self):
        soup = BeautifulSoup(self.document, self.parser)
        result = {}
        for each in soup.select('div[class*="iva-item-body"]'):
            product_price = each.select('span[class*="price-price-"]')[0] \
                .getText()
            product_title = each.find('h3').getText()
            result[product_title] = product_price
        for title, price in result.items():
            print(title, price)
        return 


url_class = GetUrl()
doc = GetDocument(url=url_class.get_url()).get_document()
avito = ToTheParse(document=doc)
avito.get_product_title_and_price()

