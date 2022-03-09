from flask import *

app = Flask(__name__)
#endpoint:端点
@app.route("/hello",methods=['GET','POST'],endpoint="hello")
def hello_world():
    return "Test String"

@app.route("/hi")
def hi():
    return "Hi"

#变量规则
#参数类型：string: int: float: path:
#<>:提取参数
@app.route("/<int:id>")
def index(id):
    if id == 1:
        return "1"
    elif id == 2:
        return "2"
    else:
        return "default"

if __name__ == "__main__":
    app.run()

