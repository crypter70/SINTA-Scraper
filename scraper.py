import scrapy

class SINTAScraper(scrapy.Spider):

    name="sinta-scraper"

    def start_requests(self):

        url = 'https://sinta.kemdikbud.go.id/affiliations'

        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # get max page
        max_page = response.css('body > div > div.col-md-8 > div.content > div.content-list.mt-5.pt-4 > nav:nth-child(12) > div > small::text').get()[10:14].strip()
        pages = int(max_page)

        # request all pages link
        for i in range(1, pages + 1):
            link = response.request.url + '?page=' + str(i)
            yield scrapy.Request(url=link, callback=self.parse_univ)


    def parse_univ(self, response):
        
        # get the univ profile link from href attribute, then follow to parse_data
        for univ in response.css('div.affil-name a::attr(href)'):
            yield response.follow(url=univ.get(), callback=self.parse_data)


    def parse_data(self, response):

        yield{
            'univ_name': response.xpath('/html/body/div/div[1]/div[2]/div/div[1]/div/div/h3/a/text()').get(),
            'alias': response.xpath('/html/body/div/div[1]/div[2]/div/div[1]/div/div/div/span[1]/text()').get().strip(),
            'address': response.xpath('/html/body/div/div[1]/div[2]/div/div[1]/div/div/div/a[1]/text()').get().strip(),
            'sinta_id': response.xpath('/html/body/div/div[1]/div[2]/div/div[1]/div/div/div/a[2]/text()').get().strip().replace('ID : ', ''),
            'pddikti_code': response.xpath('//i[@class="zmdi zmdi-code ml-2"]/following-sibling::text()').get().strip().replace('CODE : ', ''),
            'author_number': response.xpath('/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[3]/text()').get(),
            'dept_number': response.xpath('/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/text()').get(),
            'journal_number': response.xpath('/html/body/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[3]/text()').get(),
            'sinta_score_overall': response.xpath('/html/body/div/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/text()').get(),
            'sinta_score_3yr': response.xpath('/html/body/div/div[1]/div[2]/div/div[3]/div/div[4]/div[1]/text()').get(),
            'sinta_score_productivity': response.xpath('/html/body/div/div[1]/div[2]/div/div[3]/div/div[6]/div[1]/text()').get(),
            'sinta_score_productivity_3yr': response.xpath('/html/body/div/div[1]/div[2]/div/div[3]/div/div[8]/div[1]/text()').get(),

            # scopus
            'scopus_docs': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/text()').get(),
            'scopus_citation': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/text()').get(),
            'scopus_cited_doc': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/text()').get(),
            'scopus_citation_per_researchers': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/text()').get(),

            # google scholar
            'gscholar_docs': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/text()').get(),
            'gscholar_citation': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[3]/text()').get(),
            'gscholar_cited_doc': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[3]/text()').get(),
            'gscholar_citation_per_researchers': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[3]/text()').get(),
            
            # wos
            'wos_docs': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/text()').get(),
            'wos_citation': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[4]/text()').get(),
            'wos_cited_doc': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[4]/text()').get(),
            'wos_citation_per_researchers': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[4]/text()').get(),
            
            # garuda
            'garuda_docs': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/text()').get(),
            'garuda_citation': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[5]/text()').get(),
            'garuda_cited_doc': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/text()').get(),
            'garuda_citation_per_researchers': response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[5]/text()').get()
        }

    