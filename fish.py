from flask import Flask

app = Flask(__name__)

from flask import render_template
from flask import request

@app.route('/', methods = ['get','post'])
def f1():
    info = request.values.to_dict()
    print(info)
    if 'passwd' in info.keys() and info['passwd'] is not None:
        passwd = request.form['passwd']
        print('==================passwd start===================')
        print(passwd)
        print('==================passwd end=====================')
        return render_template('ustcLogin.html', flag = info['flag'], cnt = info['cnt'])
    
    return render_template('ustcLogin.html', flag = 0, cnt = 0)


# @app.route('/home', methods = ['get', 'post'])
# def f2():
#     passwd = request.form['passwd']
#     print('==================passwd start===================')
#     print(passwd)
#     print('==================passwd end=====================')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')

