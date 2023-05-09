#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder='', template_folder='')
app.config['SCHEDULER_API_ENABLED'] = True

# ---------- 路由設定 ----------
@app.route('/')
def index():  # 首頁
    return render_template('index.html')

# ---------- 以下為資料庫API ----------
@app.route('/sendNotify', methods={'POST'})
def sendNotify():  # 取得指定的訂單資料
    data = request.get_json()

    requests.post(
            'https://notify-api.line.me/api/notify',
            data={"message": data['message']},
            headers={"Authorization": "Bearer BEpyNQaJCOOqcmhMO7x5caigZLQOg4aM8gmIpRS4iKU"})
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)