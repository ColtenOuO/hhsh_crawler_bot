from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
## 延遲時間相關
import time
## 單元測試模組，線性測試用不到
import unittest

def get_announcement():
 
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)
    driver.get("https://www.hhsh.tn.edu.tw/home")
    
    actions = ActionChains(driver)


    rt = ""
    for i in range(1,2):

        str1 = '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/table/tbody/'
        str2 = 'tr[' + str(i) + ']/td[3]/a'
        data = driver.find_element(By.XPATH,str1+str2)

        actions.move_to_element(data).perform()
        actions.double_click(data).perform()
        time.sleep(2)

        txt =  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]')
        print(txt.text)

        rt += ('【新化高中校網公告' + str(i) + '】' + data.text + '\n')

    return rt