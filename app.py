from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

    @app.route('/baseball')
def baseball():
    return 'Hello, baseball!'

    @app.route('/method',methods=['GET', 'POST'])
def method():
        if request.method == 'GET':
            return "GET으로 전달"
         else:
                return "POST로 전달"

    if __name__ == '__main__':
    app.run()