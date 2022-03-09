# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/2/23 3:48 PM
# 文件名称:FlaskFormDemo.PY
# 开发工具:PyCharm

#request 包含前端发送过来的所有数据
#关于表单提交功能

from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/index", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print('name = ',name)
        print('password = ',password)
        return 'success'


if __name__ == '__main__':
    app.run()