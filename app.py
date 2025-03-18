from redis import Redis
from flask import Flask
import os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route('/')
def hello_world():  # put application's code here
    redis.incr('hits')
    return 'Welcome to my homework 3. You have seen this page {0} times.'.format(redis.get('hits'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
