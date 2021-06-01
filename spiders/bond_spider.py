import scrapy
import pandas as pd


class BondSpider(scrapy.Spider):
    name = "first"

    def start_requests(self):
        return [scrapy.FormRequest('https://www.artemis.bm/deal-directory', callback=self.get_links)]

    def get_links(self, response):
        next_page_table = response.css('#table-deal tbody tr')
        urls = []
        for next_page in next_page_table:
            path = next_page.css('td a::attr(href)').get()
            # urls.append(path)

            yield scrapy.Request(url=path, callback=self.parse)
        # print(len(urls))

    def parse(self, response):
        items = []
        item = {}
        columns = []


        for info in response.css('#info-box ul li'):
            columns.append(info.css('strong::text').get())
            item = {}
            item[info.css('strong::text').get()] = info.css('li::text').get().strip()
            items.append(item)
        combinedItems = {k:v for x in items for k,v in x.items()}
        expected_loss = response.css("div.pf-content").re(r'(?<=expected\sloss\sof\s)[^%]*')
        expected_loss2 = response.css("div.pf-content").re(r'(?<=expected\sloss\sis\s)[^%]*')
        attachment_probability = response.css("div.pf-content").re(r'(?<=attachment\sprobability\sof\s)[^%]*')
        combinedItems['Expected Loss'] = expected_loss
        combinedItems['Expected Loss2'] = expected_loss2
        combinedItems['Attachment Probability'] = attachment_probability
        yield combinedItems
        # toDF = [combinedItems]
        # x = pd.DataFrame(toDF, columns=columns)

        # expected_loss = response.css("div.pf-content").re(r'(?<=expected\sloss\sof\s)[^%]*')
        # x['Expected Loss'] = expected_loss
        # # yield x
        # yield x.to_csv("r.csv", index=False)

    