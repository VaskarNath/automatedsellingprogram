# -*- coding: utf-8 -*-
import scrapy
import csv


# output from url_scraper
urls = ['https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Introduction+of+Functional+Analysis+Angus+E.+Taylor', 'https://www.amazon.ca/s?k=Linear+Differential+Operator+Cornelius+Lanczos&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Time+Series+Analysis%3A+Forecasting+and+Control+Box%2C+Jenkins&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Measure+and+Integration+Bernerian&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=General+Statistics+Chase%2C+Bown&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Introduction+to+Linear+Regression+Analysis+Montgomery%2C+Peck%2C+Vining&ref=nb_sb_noss', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Introduction+to+Time+Series+and+Forecasting+Brockwell%2C+Davis', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Probability+and+Statistics+for+Engineering+and+the+Sciebces+Devore', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Multiple+Time+Series+Hannan', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Lebesque+Integration+Williamson', 'https://www.amazon.ca/s?k=Introduction+to+Mathematical+Analysis+Eaves&ref=nb_sb_noss', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Real+Analysis+Royden', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Regression+Analysis+Concepts+and+Applications+Graybill%2C+Iyer', 'https://www.amazon.ca/s?k=Testing+Statistical+Hypothesis+Lehmann&ref=nb_sb_noss', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Linear+Statistical+Inference+and+its+Applications+Rao', 'https://www.amazon.ca/s?k=Principles+of+Econometrics+Theil&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Probability+and+Statistical+Inference+I+Kalbfleisch&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=The+History+of+Statistics%3A+The+Measurement+of+Uncertainty+before+1900+Stigler&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Continuous+Univariate+Distributions+I+Johnson%2C+Kotz&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Distributions+in+Statistics%3A+Continuous+Univariate+Distributions+2+Johnson%2C+Kotz&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=An+Introduction+to+Mathematical+Statistics+Brunk&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=The+Lognormal+Distribution+with+Special+Reference+to+its+Uses+in+Economics+Aitchison%2C+Brown&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Discrete+Distributions+Johnson%2C+Kotz&ref=nb_sb_noss', 'https://www.amazon.ca/s?k=Analysis+of+Variance+Guenther&ref=nb_sb_noss', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=A+First+Course+in+Numerical+Analysis+Ralston%2C+Rabinowitz', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=The+Theory+of+Interest+Kellison', 'https://www.amazon.ca/s?k=The+Theory+of+Statistical+Inference+Zacks&ref=nb_sb_noss', 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Testing+Statistical+Hypothesis+Lehmann']

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.ca']

    def parse(self, response):

        all_the_books = response.xpath("//div[@data-component-type='s-search-result']")
        print(len(all_the_books))

        for book in all_the_books:
            title = book.xpath(".//span[@class='a-size-medium a-color-base a-text-normal']/text()").extract_first()
            author = book.css(".a-color-secondary .a-size-base:nth-child(2)").css("::text").extract_first()
            price = book.css(".a-price-whole::text").extract_first(default='0')

            row = [title, price, author]
            # Open file in append mode
            with open("../data.csv", 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = csv.writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(row)



