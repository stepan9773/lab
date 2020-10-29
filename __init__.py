__version__ = '0.1.0'
from flask import Flask
app = Flask(__name__)
@app.route('/iter/<int:index>')
def iter(index):
    return  ' '.join([str(i) for i in range(index)])
@app.route('/api/v1/<string:index>')
def hello_index(index):

    return  'Hello World ' + index[str(index).rfind("-")+1:] , print(" HTTP/1.1 OK 200")

if __name__ == '__main__':
    import sys
    print(sys.executable)
    app.run(port=8000,host='localhost')