# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pdf_downloader.items import PdfDownloaderItem


class PdfspiderSpider(scrapy.Spider):
    name = 'downloader'
    #allowed_domains = ['bitsavers.org/pdf/sony/floppy']
    start_urls = ['http://bitsavers.org/pdf/sony/floppy']

    def parse(self, response):
        for href_in_page in response.xpath("//a[contains(@href,'.pdf')]"):
            loader = ItemLoader(item=PdfDownloaderItem(), selector=href_in_page)
            relative_url = href_in_page.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            loader.add_xpath('pdf_name', './text()')
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print(absolute_url)
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            yield loader.load_item()
