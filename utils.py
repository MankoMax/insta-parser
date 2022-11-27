from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
import moviepy.editor as mp
from shazamio import Shazam
from consolehelper import *




def loginToInsta(driver):
    clearConsole()
    text_box = driver.find_element(by=By.NAME, value="username")
    text_box.clear()
    text_box.send_keys(input(
        "Enter your account name/phone number/e-mail:- "))
    time.sleep(2)
    waitingMessage()
    
    clearConsole()
    text_box = driver.find_element(by=By.NAME, value="password")
    text_box.clear()
    text_box.send_keys(hidenPassword())
    time.sleep(2)
    waitingMessage()
    
    clearConsole()
    text_box.send_keys(Keys.ENTER)
    time.sleep(5)
    waitingMessage()
    

def downloadVideo(driver):
    clearConsole()
    driver.get(input(
        "Enter the post link to video:- "))
    time.sleep(2)
    waitingMessage()
    video_url = driver.find_element(
        by=By.TAG_NAME, value='video').get_attribute('src')
    
    clearConsole()
    r = requests.get(video_url, stream = True)
    with open('1.mp4', 'wb') as f:
      for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
          f.write(chunk)
          

def videoToWavConvert():
    clearConsole()
    clip = mp.VideoFileClip("1.mp4")
    clip.audio.write_audiofile("1.wav")
    

async def recognizeSong():
    clearConsole()
    waitingMessage()
    shazam = Shazam()
    out = await shazam.recognize_song('1.wav')
    clearConsole()
    print("Song name:- ")
    print(out['track']['subtitle'] + " - " + out['track']['title']) 
  
  
def removeFiles():
    os.remove("1.mp4")
    os.remove("1.wav")
  
    
def stopApp():
    exit()

