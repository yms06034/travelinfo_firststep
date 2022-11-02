from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pymysql
from sqlalchemy import create_engine


# Options Setting
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('incognito')
# Header Setting
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

browser = webdriver.Chrome("./chromedriver.exe" ,options=options)

browser.get("https://korean.visitkorea.or.kr/list/all_list.do?choiceTag=&choiceTagId=")

browser.implicitly_wait(30) # waiting

def finds(css_selector):
  return browser.find_elements(By.CSS_SELECTOR, css_selector)

def find(css_selector):
  return browser.find_element(By.CSS_SELECTOR, css_selector)

def finds_xpath(xpath):
    return browser.find_elements(By.XPATH, xpath)

click_list = ['62492549-e40b-4f9d-8f79-48f9eb50d39b', '00bb51f9-922d-46f4-83e5-3db360575b96', 'e378af13-f6d1-11e8-9488-02001c6b0001',
                '01161a8e-fbe7-40b7-a0ba-54aace3144ab', 'c2d6e663-6186-11eb-b08c-0050569dc2b9', 'e36a319c-7cf2-11e9-9488-02001c6b0001',
                '423a9351-bb43-45b8-97d9-2ca01b96bd10', 'af5e51e3-83df-11e8-8165-020027310001', '898aa43b-9714-11e8-8165-020027310001']

for i in click_list:
    click_tag = find(f"li[id='{i}'] > button")
    click_tag.click()
    time.sleep(3)

time.sleep(5)

img_scr = []
title = []
place_info = []
tag_info= []

for i in range(1, 500):
    search_imgs = finds("div[class='photo'] > a > img")
    for img in search_imgs:
        img_scr.append(img.get_attribute('src'))

    seacrh_text = finds("div[class='tit'] > a")
    for text in seacrh_text:
        title.append(text.text)

    search_place = finds_xpath("//*/div/div/ul/li/div/p[1]")
    for place in search_place:
        place_info.append(place.text)

    serach_tag = finds_xpath("//*/div/div/ul/li/div/p[3]")
    for tag in serach_tag:
        tag_info.append(tag.get_attribute('textContent'))

    click_btn = find(f"div[class='page_box'] > a[id='{i}']")
    click_btn.click()

    time.sleep(5)

browser.close()
print(type(img_scr))
print(type(title))
print(type(place_info))
print(type(tag_info))
# items = [item for item in zip(img_scr, title, place_info, tag_info)]

data = {"img_scr" : img_scr, "title":title, "place":place_info, "tag":tag_info}
df = pd.DataFrame(data)

# Data preprocessing
df = df.drop_duplicates()

df['title'] = df['title'].str.replace('\[한국관광 품질인증/Korea Quality]', '')
df['title'] = df['title'].str.replace('\[유네스코 세계유산]', '')
df['title'] = df['title'].str.replace('\[유네스코 세계문화유산]', '')
df['title'] = df['title'].str.replace('\[한국관광품질인증/Korea Quality]', '')
df['title'] = df['title'].str.replace('\[일주일 살아보기 시즌 2]', '')
df['title'] = df['title'].str.replace('(Game Show & Trade, All-Round)', '')
df['title'] = df['title'].str.replace('\(\)', '')

dr = df[df['img_scr'].str.contains('undefined')].index
df.drop(dr, inplace=True)
df.reset_index(drop=True, inplace=True)

df.columns = df.columns.str.replace(' ', '')

df_2 = df.copy()

df_2['tag'] = df_2['tag'].str.replace('#', ' ')
df_2['tag'] = df_2['tag'].str.lstrip()
df_2['title'] = df_2['title'].str.replace('\,', '')

# mysql database connect
DB_CONNECT_PATH = 'mysql+pymysql://root:password@localhost/klook?charset=utf8'

engine = create_engine(DB_CONNECT_PATH)
conn = engine.connect()

df.to_sql(name='travelinfo', con=engine, if_exists='replace')
conn.close()