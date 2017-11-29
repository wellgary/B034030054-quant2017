import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    df = pd.read_csv('nyse_companylist.csv')
    return df._repr_html_()

@app.route('/nyse/<symbol>')
def nyse_company(symbol):
    symbolfull = pd.read_csv('nyse_companylist.csv').Symbol
    for i,j in enumerate(symbolfull):
        if symbol in j:
            number = i
    df = pd.read_csv('nyse_companylist.csv').iloc[number]
    df1 = pd.DataFrame([df])
    return df1._repr_html_()

@app.route('/nasdaq')
def nasdaq():
    df = pd.read_csv('nasdaq_companylist.csv')
    return df._repr_html_()

@app.route('/nasdaq/<symbol>')
def nasdaq_company(symbol):
    symbolfull = pd.read_csv('nasdaq_companylist.csv').Symbol
    for i,j in enumerate(symbolfull):
        if symbol in j:
            number = i
    df = pd.read_csv('nasdaq_companylist.csv').iloc[number]
    df1 = pd.DataFrame([df])
    return df1._repr_html_()

@app.route('/amex')
def amex():
    df = pd.read_csv('amex_companylist.csv')
    return df._repr_html_()

@app.route('/amex/<symbol>')
def amex_company(symbol):
    symbolfull = pd.read_csv('amex_companylist.csv').Symbol
    for i,j in enumerate(symbolfull):
        if symbol in j:
            number = i
    df = pd.read_csv('amex_companylist.csv').iloc[number]
    df1 = pd.DataFrame([df])
    return df1._repr_html_()

if __name__=="__main__":
    app.run()
