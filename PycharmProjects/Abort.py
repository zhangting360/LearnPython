# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/3/9 3:19 PM
# 文件名称:Abort
# 开发工具:PyCharm

#raise 主动抛出异常
#abort 在网页中抛出异常

from flask import Flask,abort,request,render_template

app = Flask(__name__)

@app.route('/index',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'zt' and password == '123':
            return 'Login Success'
        else:
            abort(404)
            return None

#自定义错误信息
@app.errorhandler(404)
def handle_404_error(err):
    return '出现错误,错误信息:%s' % err

if __name__ == '__main__':
    app.run()

