import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Crawling():
    url = 'https://www.kookmin.ac.kr/user/unLvlh/lvlhSpor/todayMenu/index.do'

    def __init__(self):
        self.response = requests.get(self.url)
        self.food_table = []

    def weekDay(self):
        return datetime.today().weekday()

    def main(self):
        if self.response.status_code == 200:
            self.html = self.response.text
            soup = BeautifulSoup(self.html, 'html.parser')
            self.food_html = soup.select_one("#frm").select("div.cont_section")
            for i in range(1, 2):

                self.food_map = {}
                self.food_map["name"] = self.food_html[i].select_one('p.cont_subtit').text

                self.table = self.food_html[i].select_one("div.food_table > table")

                self.cafe_food = {}

                self.index = [element.text for element in self.table.select("thead > tr > th")]
                for cafe in self.table.select("tbody > tr"):
                    self.cafe_name = cafe.select_one("td").text
                    #print(self.cafe_name)
                    self.cafe_food[self.cafe_name] = []
                    for food in cafe.select("td"):
                        self.cafe_food[self.cafe_name].append(food.text)
                self.food_map["menu"] = self.cafe_food

                self.food_table.append(self.food_map)
        return self.food_table

    def todayMenu(self, restaurant):
        if restaurant == "가마중식":
            return self.main()[0]["menu"]["가마중식"][self.weekDay() + 2].strip()
        elif restaurant == "누들송(면)중식":
            return self.main()[0]["menu"]["누들송(면)중식"][self.weekDay() + 2].strip()
        elif restaurant == "인터쉐프중식":
            return self.main()[0]["menu"]["인터쉐프중식"][self.weekDay() + 2].strip()
        elif restaurant == "데일리밥중식":
            return self.main()[0]["menu"]["데일리밥중식"][self.weekDay() + 2].strip()


if __name__ == "__main__":
    print(Crawling().todayMenu("인터쉐프중식"))



