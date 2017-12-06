import requests
import pandas as pd
import io
from datetime import datetime

def get_data(symbol,startdate):
    url= "http://finance.google.com/finance/historical"
    params = {}
    params['q'] = symbol
    params['startdate'] = startdate
    params['output'] = 'csv'
    r = requests.get(url , params = params)
    return(r.text)

df = get_data('TSLA',datetime(2016,1,1))
data = pd.read_csv(io.StringIO(df))
print(data.head())
print(data.tail())
