from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('graph.html')

@app.route('/position') #db에서 데이터 불러서 json 형태로 리턴해 주는 서버
def position():
    con = sqlite3.connect('new.db',isolation_level=None)
    cur = con.cursor()
    cur.execute('select x, y from new order by DateTime desc limit 1') # db에서 가장 최근 데이터 불러오기
    rows = cur.fetchone()

    x = rows[0] # x값 저장
    y = rows[1] # y값 저장

    if rows:
        return jsonify({'x': x, 'y': y}) # 값 있으면 해당 값 전달
    else:
        return jsonify({'x': 0, 'y': 0}) # 값 없으면 (0, 0) 전달

if __name__ == '__main__':
    app.run(host='localhost', port=5000)