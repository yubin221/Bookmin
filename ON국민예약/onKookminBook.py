from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import calendar
import time


class OnKookminBook:
    def __init__(self):
        self.dateTable = {"09:00":"", "09:30":"", "10:00":"", "10:30":"", "11:00":"", "11:30":"", "12:00":"", "12:30":"", "13:00":"", "13:30":"", "14:00":"", "14:30":"", "15:00":"", "15:30":"", "16:00":"", "16:30":"", "17:00":"", "17:30":"", "18:00":"", "18:30":"", "19:00":"", "19:30":"", "20:00":"", "20:30":""}
        self.driver = None
        self.year = 0
        self.month = 0
        self.day = 0
        self.plus = None
        self.minus = None

    def quitDriver(self):
        self.driver.quit()

    def plusPage(self, n):
        for i in range(n):
            self.plus.click()
        time.sleep(1)

    def minusPage(self, n):
        for i in range(n):
            self.minus.click()
        time.sleep(1)

    def setDriver(self):
        self.driver = self.setChromeDriver()

    def setChromeDriver(self):
        chromeOption = webdriver.ChromeOptions()
        # chromeOption.add_argument("headless") # 백그라운드에서 실행하는 방법
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOption)
        driver.maximize_window()
        driver.get("https://portal.kookmin.ac.kr/por/ln")
        return driver

    def loginOnkookmin(self, dvr, id, pw):
        idBox = dvr.find_element(By.XPATH, '//*[@id="loginId"]')
        pwBox = dvr.find_element(By.XPATH, '//*[@id="pswd"]')
        idBox.send_keys(id)
        pwBox.send_keys(pw)
        pwBox.send_keys(Keys.ENTER)
        time.sleep(2)

    def toPortal(self,dvr):
        step1 = dvr.find_element(By.XPATH, '/html/body/div/div[1]/header/article/div[1]/nav/article')
        step1.click()
        step2 = dvr.find_element(By.XPATH,
                                 '/html/body/div/div[1]/header/article/div[1]/nav/article/nav/div[1]/ul/li[5]/a')
        step2.click()

        step3 = dvr.find_element(By.XPATH,
                                 '/html/body/div/div[1]/header/article/div[1]/nav/article/nav/div[2]/div[2]/div[3]/ul/li['
                                 '2]/a')  # 운동장/테니스장/체육관 예약
        step3.click()
        time.sleep(13)
        step4 = dvr.find_element(By.XPATH,
                                 '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main.form.btn_height2"]')

        self.plus = dvr.find_element(By.XPATH,
                                '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main.form.btn_height"]')
        self.minus = dvr.find_element(By.XPATH,
                                 '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main.form.btn_height2"]')
        time.sleep(1)
        print("로딩끝")

    def getDateSchedule(self, dvr, y, m, d):  # 코드를 재사용하는부분이있어서 기술적으로 크롤링을 못하겠어요
        self.dateTable = {"09:00": "", "09:30": "", "10:00": "", "10:30": "", "11:00": "", "11:30": "", "12:00": "",
                          "12:30": "", "13:00": "", "13:30": "", "14:00": "", "14:30": "", "15:00": "", "15:30": "",
                          "16:00": "", "16:30": "", "17:00": "", "17:30": "", "18:00": "", "18:30": "", "19:00": "",
                          "19:30": "", "20:00": "", "20:30": ""}

        self.plusPage(4)
        html = dvr.page_source

        temp = calendar.monthrange(y, m)[0] + 1
        temp = temp - 7 if temp > 7 else temp
        temp += d
        temp = str(temp) if temp > 9 else "0" + str(temp)
        soup = BeautifulSoup(html, 'html.parser')
        div_origin = soup.find('div', {
            'id': 'mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main.form.grd_date' + temp + '.body'})
        divs = div_origin.find_all('div', {'class': "GridRowControl row nexatransform"})
        for div in divs:
            divs_ = div.find_all('div')
            d = str(divs_[5])[str(divs_[5]).find(">") + 1:-6]
            e = str(divs_[8])[str(divs_[8]).find(">", str(divs_[8]).find(">") + 1) + 1:-12]
            self.dateTable[e] = d
        print(self.dateTable)

    def bookTime(self, dvr, y, m, d, whenli, purpose):
        temp = calendar.monthrange(y, m)[0] + 1
        temp = temp - 7 if temp > 7 else temp
        temp += d
        temp = str(temp) if temp > 9 else "0" + str(temp)

        self.minusPage(2)

        bookBtn = dvr.find_element(By.XPATH,
                                   '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main.form.grd_date' + temp + '.head.gridrow_-1.cell_-1_2"]')
        bookBtn.click()
        time.sleep(5)
        #___

        for i in whenli:
            temp_index = str(i)
            temp_checkbox = dvr.find_element(By.XPATH, '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.grd_afac622_00.body.gridrow_' + temp_index + '.cell_' + temp_index + '_0.cellcheckbox:icontext"]')
            temp_checkbox.click()

        purposeBar = dvr.find_element(By.XPATH, '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form.div_Work.form.div_main02.form.edt_main_usePurpsCtnt:input"]')
        purposeBar.send_keys(purpose)
        time.sleep(10)

if __name__ == "__main__":
    okb = OnKookminBook()
    okb.setDriver()
    okb.loginOnkookmin(okb.driver, okb.id, okb.pw)
    okb.toPortal(okb.driver)
    okb.getDateSchedule(okb.driver, 2022, 12, 4)
    okb.bookTime(okb.driver, 2022, 12, 7, [0,1,2], "a")
    while True:
        pass
