from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def setChromeDriver():
    chromeOption = webdriver.ChromeOptions()
    # chromeOption.add_argument("headless") # 백그라운드에서 실행하는 방법
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOption)
    return driver


def loginOnkookmin(dvr, id, pw):
    idBox = dvr.find_element(By.XPATH, '//*[@id="loginId"]')
    pwBox = dvr.find_element(By.XPATH, '//*[@id="pswd"]')
    idBox.send_keys(id)
    pwBox.send_keys(pw)
    pwBox.send_keys(Keys.ENTER)
    time.sleep(0.8)


def toPortal(dvr):
    step1 = dvr.find_element(By.XPATH, '/html/body/div/div[1]/header/article/div[1]/nav/article')
    step1.click()
    step2 = dvr.find_element(By.XPATH, '/html/body/div/div[1]/header/article/div[1]/nav/article/nav/div[1]/ul/li[5]/a')
    step2.click()

    step3 = dvr.find_element(By.XPATH,
                             '/html/body/div/div[1]/header/article/div[1]/nav/article/nav/div[2]/div[2]/div[3]/ul/li['
                             '2]/a')  # 운동장/테니스장/체육관 예약
    step3.click()
    time.sleep(15)
    step3_1 = dvr.find_element(By.XPATH,
                               '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form'
                               '.div_Work.form.div_main.form.chk_ok:icontext"]/div')
    step3_1.click()
    time.sleep(15)


def setDate(dvr, y, m):
    dateBox = dvr.find_element(By.XPATH,
                               '//*[@id="mainframe.HFrame.VFrame.VMainFrame.HFrameWork.WorkFrame.ChildFrame.form'
                               '.div_Work.form.div_main.form.msk_resveMmCd:input"]')
    dateBox.send_keys(y)
    dateBox.send_keys(m)

def getDateSchedule(dvr,d):
    pass


if __name__ == "__main__":
    driver = setChromeDriver()
    driver.get("https://portal.kookmin.ac.kr/por/ln")
    loginOnkookmin(driver, "dlehdrb0822", "Onkdong26110749!")
    toPortal(driver)
    time.sleep(10)
