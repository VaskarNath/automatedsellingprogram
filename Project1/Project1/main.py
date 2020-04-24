from amazon_spider import AmazonSpiderSpider
from scrapy.crawler import CrawlerProcess
from url_scraper import get_urls
from analyze_data import analyze_data


def main():

    # start_urls = get_urls()
    #
    # process = CrawlerProcess()
    # process.crawl(AmazonSpiderSpider, start_urls=start_urls)
    # process.start()

    analyze_data()


if __name__ == "__main__":
    main()
