import requests
from bs4 import BeautifulSoup

url = 'https://www.kookmin.ac.kr/user/unLvlh/lvlhSpor/todayMenu/index.do'

response = requests.get(url)

food_table = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    food_html = soup.select_one("#frm").select("div.cont_section")
    for i in range(1, 4):

        food_map = {}
        food_map["name"] = food_html[i].select_one('p.cont_subtit').text

        table = food_html[i].select_one("div.food_table > table")

        cafe_food = {}

        index = [element.text for element in table.select("thead > tr > th")]
        for cafe in table.select("tbody > tr"):
            cafe_name = cafe.select_one("td").text
            print(cafe_name)
            cafe_food[cafe_name] = []
            for food in cafe.select("td"):
                cafe_food[cafe_name].append(food.text)
        food_map["menu"] = cafe_food

        food_table.append(food_map)
print(food_table)














# import requests
# import re
# from bs4 import BeautifulSoup
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
# url = "https://www.kookmin.ac.kr/user/unLvlh/lvlhSpor/todayMenu/index.do"
#
# res = requests.get(url, headers=headers)
# html = res.content.decode('utf-8','replace')
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find_all('#frm > div:nth-child(4) > div > table > tbody > tr.first > td:nth-child(3)')[0].text)
# print(soup.title)
#
# #dinings = soup.find_all("input", attrs={"name":"aa"})
# #print(dinings[100].find_next_sibling())
# dinings = soup.select("td")
# print(dinings)
#
#
#
# # res = requests.get(url, headers = headers)
# # res.raise_for_status()
# # soup = BeautifulSoup(res.text, "lxml")
# # print(soup.title)
# # # dinings = soup.find_all("td", attrs={"class":"ft1"})
# # # print(dinings.get_text())
#
#
# # res = requests.get(url, headers=headers)
#
# ##frm > div:nth-child(4) > div > table > tbody > tr.first > td:nth-child(3)
#
# # 1:월 2:화 3:수 4:목 5:금
# def crawlingDict(weeknumber):
#     pass


