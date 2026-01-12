from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'vannakam, valga valamudan'
@app.route('/tamizh')
def vazhga():
    return 'tamizh vazhga'

if __name__ == '__main__':
    app.run(debug=True)