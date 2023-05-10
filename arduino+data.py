#아두이노로 조이스틱 센서 값 읽어서 database에 저장하는 코드

import sqlite3
import datetime
import serial

coms = serial.Serial("COM5", baudrate=9600) #시리얼 포트 com5에 연결

con = sqlite3.connect('new.db',isolation_level=None) #데이터베이스에 연결
cur = con.cursor()

def dataplus(x, y): #데이터베이스에 센서값 저장하는 함수
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    cur.execute('INSERT INTO new (DateTime, x, y) VALUES (?, ?, ?)', (nowDatetime, x, y))

while True: #조이스틱 센서로 얻은 x 좌표 값과, y 좌표 값을 dataplus 함수를 통해 무한 저장
    readed = coms.readline()
    readed = readed.decode().strip()

    x = float(readed[:4])
    y = float(readed[-4:])

    print(x, y)
    dataplus(x, y)

