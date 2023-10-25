# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:47:23 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
data = requests.get(url,headers = header)
data.encoding = 'utf-8'
data = data.text.strip()
soup = BeautifulSoup(data,'html.parser')
rate = soup.find(id = 'exchangeRate')
table = rate.find('table')
tbody = table.find('tbody')
td = tbody.find_all('td')
for row in td:
    print(row.text.strip())