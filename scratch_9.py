from selenium import webdriver as web
import requests
from bs4 import BeautifulSoup


login_data = {
    'name' : 'vaskar.nath@outlook.com',
    'pass' : 'Ri0*de*janeiro',
    'form_id' : " ",
    'op' : 'Login'
}

with requests.session() as s:
    url = 'https://www.ebay.ca/signin/s'
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.find('input', attrs={'name': 'us_id'}))
    login_data['form_id'] = soup.find('input', attrs={'name': 'usid'})['value']

    r = s.post(url, data=login_data)
    print(r.content)
