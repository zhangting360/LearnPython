# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/3/9 2:28 PM
# 文件名称:JsonResponse
# 开发工具:PyCharm

#json数据

from flask import Flask,make_response,json,jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/index')
def index():
    data = {'name':"张二"}
    # response = make_response(json.dumps(data,ensure_ascii=False))
    # response.mimetype = "application/json"
    # return response

    return jsonify(data)

if __name__ == "__main__":
    app.run()