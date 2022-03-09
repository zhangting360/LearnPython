# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/3/9 2:18 PM
# 文件名称:Redirection
# 开发工具:PyCharm

#重定向 302

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return redirect(url_for("hello"))
    # return redirect('http://www.bilibili.com')

@app.route('/')
def hello():
    return 'this is hello'

if __name__ == '__main__':
    app.run()