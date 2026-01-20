## Building URL dynamically
## Varaible Rules and URL Building

from flask import Flask,redirect,url_for

app = Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to my youtube channel"

## Varaible Rules and URL Building
@app.route('/pass/<int:score>')
def success(score):
    return "PASS"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Fail"+ str(score)


@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug=True)