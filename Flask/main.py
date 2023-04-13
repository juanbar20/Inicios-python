from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response



@app.route('/')
def hello():
    user_ip = request.remote_addr
    return "Hello World Flask, su IP es {}".format(user_ip)