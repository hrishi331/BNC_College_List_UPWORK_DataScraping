# Extracted https://www.bncollege.com/campus-stores/ 
# Upwork project
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.bncollege.com/campus-stores/"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'no-cache',
  'pragma': 'no-cache',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'Cookie': '_gcl_au=1.1.2093043135.1750309788; _gid=GA1.2.1019168887.1750309788; _gd_visitor=317fb936-9797-4b59-8a75-74b2de83e6f2; _gd_session=6940110e-c0fe-4e5f-8e9f-b1cf474cdeb0; hubspotutk=68bf033d097f685a765a5aec9d5a1098; visitor_id814533=371546137; visitor_id814533-hash=1ab9f3a25aa9dcc44248fcfec36bfa7f39e0413593d8057d0d5344ca11668d2e2222cc15d6a6a4c5677430c87c157d19c7f0b6f7; _gat_UA-27629003-1=1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+19+2025+12%3A25%3A23+GMT%2B0530+(India+Standard+Time)&version=202505.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.bncollege.com%2Fcampus-stores%2F&groups=C0010%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1; _ga=GA1.2.1572546948.1750309788; _ga_0XTXH054VW=GS2.1.s1750315085$o2$g1$t1750316123$j60$l0$h0; __hstc=77438090.68bf033d097f685a765a5aec9d5a1098.1750309788904.1750315086102.1750316125049.3; __hssrc=1; __hssc=77438090.1.1750316125049'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.content,'html.parser')

l = soup.find_all('script')[21].text.split(' = ')[1].split(";")[0]
l = json.loads(l)

l = pd.DataFrame(l)

l.to_csv(r"Database/SchoolStoreList.csv",index=False)