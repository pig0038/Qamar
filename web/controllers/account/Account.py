# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template

route_account = Blueprint('account_page', __name__)

@route_account.route('/index')
def index():
    return render_template('account/index.html')

@route_account.route('/edit')
def info():
    return render_template('account/info.html')

@route_account.route('/reset-pwd')
def set():
    return render_template('account/index.html')