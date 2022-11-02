import pandas as pd
import pymysql
from sqlalchemy import create_engine

DB_CONNECT_PATH = 'mysql+pymysql://root:password@localhost/klook?charset=utf8'

engine = create_engine(DB_CONNECT_PATH)
conn = engine.connect()

SQL_SEOUL = """SELECT * FROM travelinfo WHERE place LIKE '서울%%';"""
SQL_BUSAN = """SELECT * FROM travelinfo WHERE place LIKE '부산%%';"""
SQL_DAEGU = """SELECT * FROM travelinfo WHERE place LIKE '대구%%';"""
SQL_INCHEON = """SELECT * FROM travelinfo WHERE place LIKE '인천%%';"""
SQL_GWANGJU = """SELECT * FROM travelinfo WHERE place LIKE '광주%%';"""
SQL_DAEJEON = """SELECT * FROM travelinfo WHERE place LIKE '대전%%';"""
SQL_UISAN = """SELECT * FROM travelinfo WHERE place LIKE '울산%%';"""
SQL_SEJONG = """SELECT * FROM travelinfo WHERE place LIKE '세종%%';"""
SQL_GYEPNGGIDO = """SELECT * FROM travelinfo WHERE place LIKE '경기%%';"""
SQL_GANGWON = """SELECT * FROM travelinfo WHERE place LIKE '강원%%';"""
SQL_CHUNGNAM = """SELECT * FROM travelinfo WHERE place LIKE '충남%%';"""
SQL_CHUNGBUK = """SELECT * FROM travelinfo WHERE place LIKE '충북%%';"""
SQL_JEONAM = """SELECT * FROM travelinfo WHERE place LIKE '전남%%';"""
SQL_JEOBUK = """SELECT * FROM travelinfo WHERE place LIKE '전북%%';"""
SQL_GYEONGNAM = """SELECT * FROM travelinfo WHERE place LIKE '경남%%';"""
SQL_GYEONGBUK = """SELECT * FROM travelinfo WHERE place LIKE '경북%%';"""
SQL_JEJU = """SELECT * FROM travelinfo WHERE place LIKE '제주%%';"""

seoul = pd.read_sql(SQL_SEOUL, engine)
busan = pd.read_sql(SQL_BUSAN, engine)
daegu = pd.read_sql(SQL_DAEGU, engine)
incheon = pd.read_sql(SQL_INCHEON, engine)
gwangju = pd.read_sql(SQL_GWANGJU, engine)
daejeon = pd.read_sql(SQL_DAEJEON, engine)
uisan = pd.read_sql(SQL_UISAN, engine)
sejong = pd.read_sql(SQL_SEJONG, engine)
gyepnggido = pd.read_sql(SQL_GYEPNGGIDO, engine)
gangwon = pd.read_sql(SQL_GANGWON, engine)
chungnam = pd.read_sql(SQL_CHUNGNAM, engine)
chungbuk = pd.read_sql(SQL_CHUNGBUK, engine)
jeonam = pd.read_sql(SQL_JEONAM, engine)
jeobuk = pd.read_sql(SQL_JEOBUK, engine)
gyeongnam = pd.read_sql(SQL_GYEONGNAM, engine)
gyeongbuk = pd.read_sql(SQL_GYEONGBUK, engine)
jeju = pd.read_sql(SQL_JEJU, engine)

seoul = seoul['title']
busan = busan['title']
daegu = daegu['title']
incheon = incheon['title']
gwangju = gwangju['title']
daejeon = daejeon['title']
uisan = uisan['title']
sejong = sejong['title']
gyepnggido = gyepnggido['title']
gangwon = gangwon['title']
chungnam = chungnam['title']
chungbuk = chungbuk['title']
jeonam = jeonam['title']
jeobuk = jeobuk['title']
gyeongnam = gyeongnam['title']
gyeongbuk = gyeongbuk['title']
jeju = jeju['title']

print(seoul)