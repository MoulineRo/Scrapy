import json
import time

import scrapy


class WorkSpider(scrapy.Spider):
    name = "work"
    allowed_domains = ["work.ua"]

    def start_requests(self):
        for url in range(1,6359):
            yield scrapy.Request(url=f'https://www.work.ua/jobs/?page={url}', callback=self.parse)
            time.sleep(0.5)

    def parse(self, response):
        for dash in range(2,17):
            x = str(response.xpath(f'//*[@id="pjax-job-list"]/div[{dash}]/h2/a/@href').extract())
            y = str(response.xpath(f'//*[@id="pjax-job-list"]/div[{dash}]/h2/a/@title').extract()).lower()
            if 'python' in y:
                out=x + ' ' + y
                with open('file.txt', 'a') as f:
                    f.write(out+'\n')
