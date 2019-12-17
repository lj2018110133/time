from flask import Flask
from study.newstudy import loginModule
from sql_study.blueprint_1 import bp
app = Flask(__name__)
"""
  这是一个注释；
"""
app.register_blueprint(loginModule)
app.register_blueprint(bp)


@app.route('/index')
def hello_world():
    return 'Hello World!1111'

if __name__ == '__main__':
    app.run() #在这里直接开启debug