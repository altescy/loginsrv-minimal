# -*- coding: utf-8 -*-
import argparse
import json
import jwt
import os
from flask import Flask, abort, request


JWT_ALGO = os.environ['LOGINSRV_JWT_ALGO']
JWT_SECRET = os.environ['LOGINSRV_JWT_SECRET']

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    try:
        user = jwt.decode(
            request.cookies.get('jwt_token'),
            JWT_SECRET,
            alg=JWT_ALGO,
        )
    except:
        abort(403)

    return '''
        <p>hello {}.</p>
        <form action="/login?logout=true" method="post">
            <input type="submit" value="logout" />
        </form>
    '''.format(user['sub'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', default=80)
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
