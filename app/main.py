# -*- coding: utf-8 -*-
import argparse
import json
import jwt
import os
from flask import Flask, redirect, request


JWT_ALGO = os.environ['LOGINSRV_JWT_ALGO']
JWT_SECRET = os.environ['LOGINSRV_JWT_SECRET']

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    try:
        user = jwt.decode(
            request.cookies.get('jwt_token'),
            JWT_SECRET,
            algorithms=[JWT_ALGO],
        )
    except:
        return redirect('http://localhost/login', code=307)

    return '''
        <p>hello {}.</p>
        <form action="/login?logout=true" method="post">
            <input type="submit" value="logout" />
        </form>
    '''.format(user['sub'])
