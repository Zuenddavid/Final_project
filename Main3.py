import requests
from bs4 import BeautifulSoup
import csv
import requests
import re
import time


cookies = {
    'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%2255e94c26-21c6-4885-b794-c0ebc9099af2%22%2C%22options%22%3A%7B%22end%22%3A%222023-05-20T07%3A41%3A38.962Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-582065-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    'userUUID': 'bd217c4b-c656-4d9b-9bd8-b61d7a659e50',
    'cookieSearch-1': '"/venta-viviendas/segovia-segovia/:1650268899748"',
    'contact0b2be20f-42f7-4005-9215-36cafd83e2da': '"{\'email\':null,\'phone\':null,\'phonePrefix\':null,\'friendEmails\':null,\'name\':null,\'message\':null,\'message2Friends\':null,\'maxNumberContactsAllow\':10,\'defaultMessage\':true}"',
    'SESSION': '503ae74b1083bcf5~0b2be20f-42f7-4005-9215-36cafd83e2da',
    'datadome': 'u.gNKhDTzlFuovc_kPG1x63FJ.D5RPd98O.0Oek8K2rKZD_X-MoMTOZdiYiYjCw9VbactEAe-b_v3gfSBzl~95flYHkxkyctI1dBcCC-y.ZBk8e5dGQ18q0IcxA9bCO',
    'didomi_token': 'eyJ1c2VyX2lkIjoiMTgwM2I5ZWItNDJhOC02NTUxLWE3MjUtYTk5MTM5OTAzYThhIiwiY3JlYXRlZCI6IjIwMjItMDQtMThUMDg6MDI6MDAuODM5WiIsInVwZGF0ZWQiOiIyMDIyLTA0LTE4VDA4OjAyOjAwLjgzOVoiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJkaXNhYmxlZCI6WyJnZW9sb2NhdGlvbl9kYXRhIiwiYW5hbHl0aWNzLUhwQkpycks3Il19LCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6bWl4cGFuZWwiLCJjOmFidGFzdHktTExrRUNDajgiLCJjOmhvdGphciIsImM6eWFuZGV4bWV0cmljcyIsImM6YmVhbWVyLUg3dHI3SGl4IiwiYzphcHBzZmx5ZXItR1VWUExwWVkiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6aWRlYWxpc3RhLUx6dEJlcUUzIiwiYzppZGVhbGlzdGEtZmVSRWplMmMiXX0sImFjIjoiQUFBQS5BQUFBIn0=',
    'euconsent-v2': 'CPXnqQAPXnqQAAHABBENCKCgAAAAAAAAAAAAAAAAAAEBoAMAAQRVJQAYAAgiqUgAwABBFUhABgACCKo6ADAAEEVQkAGAAIIqjIAMAAQRVFQAYAAgiqAA.YAAAAAAAAAAA',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': f"atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%2255e94c26-21c6-4885-b794-c0ebc9099af2%22%2C%22options%22%3A%7B%22end%22%3A%222023-05-20T07%3A41%3A38.962Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-582065-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; userUUID=bd217c4b-c656-4d9b-9bd8-b61d7a659e50; cookieSearch-1=\"/venta-viviendas/segovia-segovia/:1650268899748\"; contact0b2be20f-42f7-4005-9215-36cafd83e2da=\"{'email':null,'phone':null,'phonePrefix':null,'friendEmails':null,'name':null,'message':null,'message2Friends':null,'maxNumberContactsAllow':10,'defaultMessage':true}\"; SESSION=503ae74b1083bcf5~0b2be20f-42f7-4005-9215-36cafd83e2da; utag_main=v_id:01803b9eb3dd0079e97829c31e2405078003d07000fb8{_sn:1$_se:7$_ss:0$_st:1650270701171$ses_id:1650267698143%3Bexp-session$_pn:7%3Bexp-session$_prevVtSource:searchEngines%3Bexp-1650271298552$_prevVtCampaignCode:%3Bexp-1650271298552$_prevVtDomainReferrer:google.com%3Bexp-1650271298552$_prevVtSubdomaninReferrer:www.google.com%3Bexp-1650271298552$_prevVtUrlReferrer:https%3A%2F%2Fwww.google.com%2F%3Bexp-1650271298552$_prevVtCampaignLinkName:%3Bexp-1650271298552$_prevVtCampaignName:%3Bexp-1650271298552$_prevVtRecommendationId:%3Bexp-1650271298552$_prevCompletePageName:11%3A%3Alisting%3A%3AresultList%3A%3Aothers%3Bexp-1650272501306$_prevLevel2:11%3Bexp-1650272501306$_prevCompleteClickName:;} datadome=u.gNKhDTzlFuovc_kPG1x63FJ.D5RPd98O.0Oek8K2rKZD_X-MoMTOZdiYiYjCw9VbactEAe-b_v3gfSBzl~95flYHkxkyctI1dBcCC-y.ZBk8e5dGQ18q0IcxA9bCO; didomi_token=eyJ1c2VyX2lkIjoiMTgwM2I5ZWItNDJhOC02NTUxLWE3MjUtYTk5MTM5OTAzYThhIiwiY3JlYXRlZCI6IjIwMjItMDQtMThUMDg6MDI6MDAuODM5WiIsInVwZGF0ZWQiOiIyMDIyLTA0LTE4VDA4OjAyOjAwLjgzOVoiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJkaXNhYmxlZCI6WyJnZW9sb2NhdGlvbl9kYXRhIiwiYW5hbHl0aWNzLUhwQkpycks3Il19LCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6bWl4cGFuZWwiLCJjOmFidGFzdHktTExrRUNDajgiLCJjOmhvdGphciIsImM6eWFuZGV4bWV0cmljcyIsImM6YmVhbWVyLUg3dHI3SGl4IiwiYzphcHBzZmx5ZXItR1VWUExwWVkiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6aWRlYWxpc3RhLUx6dEJlcUUzIiwiYzppZGVhbGlzdGEtZmVSRWplMmMiXX0sImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CPXnqQAPXnqQAAHABBENCKCgAAAAAAAAAAAAAAAAAAEBoAMAAQRVJQAYAAgiqUgAwABBFUhABgACCKo6ADAAEEVQkAGAAIIqjIAMAAQRVFQAYAAgiqAA.YAAAAAAAAAAA",
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',}

def get_pages():
    url = "https://www.idealista.com"
    next_page = url+"/venta-viviendas/madrid-madrid/"
    stuff = []
    urls = []
    count = 1

    while next_page and count < 6:
        urls.append(next_page)
        responses = requests.get(next_page, headers=headers, cookies = cookies)
        soupe = BeautifulSoup(responses.content, "html.parser")
        stuff.append(soupe.find_all("section", "items-container"))
        next_href = soupe.find('li', attrs={'class': 'next'})
        if next_href:
            next_page = url+next_href.find("a")['href']
        else:
            next_page = None
        print(next_page)
        count += 1
        print("Wainting 15 seconds")
        time.sleep(15)

    return urls


def csv_file(lists):
  with open("housingmarket_madrid4.csv", "w", encoding="utf8") as f:
      writer = csv.writer(f)
      headers = ['Name', "Location", "Price", "Rooms", "Surface", "Floor"]
      f.write(",".join(headers))
      f.write("\n")

      for x in lists:
          names = x.findAll('a', 'item-link')
          prices = x.findAll('span', 'item-price h2-simulated')
          rest = x.findAll('div', 'item-detail-char')
      names_title = []
      names_location = []
      #names_city = []
      for name in names:
          names_title.append(name.text.split(",")[0])
          names_location.append(name.text.split(",")[1])
          #names_city.append(name.text.split(",")[2])

      price_list = []
      for price in prices:
          price_list.append(price.text)
      rooms_list = []
      surface_list = []
      floor_list = []

      for descr in rest:
          rooms_list.append(descr.text.split('\n')[1])
          surface_list.append(descr.text.split('\n')[2])
          floor_list.append(descr.text.split('\n')[3])

      for all_info in zip(names_title,names_location, price_list, rooms_list, surface_list, floor_list):
          f.write(",".join(all_info))
          f.write("\n")


def csv_file2(lists):
  with open("housingmarket_madridOG.csv", "a", encoding="utf8") as f:

      for x in lists:
          names = x.findAll('a', 'item-link')
          prices = x.findAll('span', 'item-price h2-simulated')
          rest = x.findAll('div', 'item-detail-char')

      names_title = []
      names_location = []

      for name in names:
          names_title.append(name.text.split(",")[0])
          names_location.append(name.text.split(",")[1])

      price_list = []

      for price in prices:
          price_list.append(price.text)

      rooms_list = []
      surface_list = []
      floor_list = []

      for descr in rest:
          rooms_list.append(descr.text.split('\n')[1])
          surface_list.append(descr.text.split('\n')[2])
          floor_list.append(descr.text.split('\n')[3])

      for all_info in zip(names_title,names_location, price_list, rooms_list, surface_list, floor_list):
          f.write(",".join(all_info))
          f.write("\n")


pages = get_pages()
for i in range(len(pages)):
  response = requests.get(pages[i], headers=headers, cookies=cookies)
  soup = BeautifulSoup(response.content, "html.parser")
  lists = soup.find_all("section", "items-container")
  if i==0:
    csv_file(lists)
  else:
    csv_file2(lists)