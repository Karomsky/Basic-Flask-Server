from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return "hello world"

@app.route('/rova')
def rova():
   return "hello rova"

if __name__ == '__main__':
      app.run(debug=True)
