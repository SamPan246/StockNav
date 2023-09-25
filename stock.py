from flask import Flask, render_template, jsonify, request
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/get_stock_data")
def get_stock_data():
    stockName = request.args.get('symbol')
    print("stockNameFromHTML= ", stockName)
    url = "https://finnhub.io/api/v1/quote?symbol="+stockName+"&token=ck7ni2hr01qp1ms30s3gck7ni2hr01qp1ms30s40"
    print("urlValue= ", url)
    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)
    stock=jsondata["c"]
    print("stock= ", stock)
    #return {"stock": jsondata}
    return render_template('index.html', stock=stock)


