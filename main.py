from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import asyncio
from utils import *




def main():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_service = Service(ChromeDriverManager().install())
  
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
  
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
  
    loginToInsta(driver)
  
    downloadVideo(driver)
  
    videoToWavConvert()
  
    asyncio.run(recognizeSong())
  
    removeFiles()
  
    stopApp()


main()


