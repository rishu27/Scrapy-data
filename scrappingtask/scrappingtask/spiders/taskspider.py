import scrapy


class TaskspiderSpider(scrapy.Spider):
    name = "taskspider"
    allowed_domains = ["www.reed.co.uk"]
    start_urls = [f"https://www.reed.co.uk/jobs/data-analyst-jobs?pageno={i}" for i in range(93)]

    def parse(self, response):
        detail=response.css('div.row')
        contract_type_element =  response.css('ul.list-group-horizontal li.list-group-item:nth-child(3)::text').get()
        for detail1 in detail:
          yield{
                'url'           :response.url,
                'Title'         :response.css('.job-card_jobResultHeading__title__IQ8iT a::text').get(),
                'Salary'        :response.css('ul.list-group-horizontal li.list-group-item::text').get(),

                'Contract Type' :contract_type_element.split(',')[0].strip(),
                'Job Type'      :contract_type_element.split(',')[1].strip(),
                'Location'      :response.css('ul.list-group-horizontal li.list-group-item:nth-child(2)::text').get()
            }
        next_page_link = response.css('a.page-link.next')

        # Check if there's a next page
        if next_page_link:
            # Follow the link to the next page
            next_page_url = detail.urljoin(next_page_link.get('href'))
            yield scrapy.Request(next_page_url, callback=self.parse)
        
        relative_url = response.css('h2.job-card_jobResultHeading__title__IQ8iT job-card_jobResultHeading__hasBadges__yeRFG a::attr(href)').get()
        # Check if there's a next page
        if relative_url:
            # Follow the link to the next page
            page_url = response.urljoin(next_page_link.get('href'))
            yield scrapy.Request(page_url, callback=self.parse_page)     
    def parse_page(self,response):
        pass