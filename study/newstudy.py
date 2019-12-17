from flask import Blueprint, render_template, request

loginModule = Blueprint('loginModule', __name__)


@loginModule.route("/login")
def login():
    return "用户登录"


@loginModule.route("/register")
def register():
    return "用户注册"


@loginModule.route("/update")
def update():
    return "用户信息修改"
