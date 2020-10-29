from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/<string:index>')
def hello_index(index):
    return  'Hello World ' + index[str(index).rfind("-")+1:] , print(" HTTP/1.1 OK 200")

if __name__ == '__main__':
    app.run(port=8000,host='localhost')