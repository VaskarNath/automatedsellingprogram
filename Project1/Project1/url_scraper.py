from selenium import webdriver as web
import pandas as pd


def get_urls():
    df = pd.read_csv("../../bookscatelogue.csv", names=["title", "edition", "author"])
    urls_to_scrape = []

    titles = df["title"].tolist()
    authors = df["author"].tolist()

    for i in range(1, len(titles)):
        # options = web.ChromeOptions()
        # options.add_argument('headless')
        driver = web.Chrome("D:\chromedriver.exe")
        driver.get("https://www.amazon.ca/")
        search_bar = driver.find_element_by_name('field-keywords')
        search_bar.send_keys("%s %s" % (titles[i], authors[i]))
        search_button = driver.find_element_by_class_name('nav-input')
        search_button.click()
        urls_to_scrape.append(driver.current_url)
        print(driver.current_url)
        driver.quit()

    print(urls_to_scrape, len(urls_to_scrape))
    return urls_to_scrape
