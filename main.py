#!/usr/bin/python3
from flask import Flask,jsonify,request,Response
from token_1 import *
from search import *
app=Flask(__name__)

requests={}
@app.route('/token')
def token():
    k=generate_api_key()
    requests[k]=0
    return jsonify({'key':k})
@app.route('/checkip/<ip>')
def checkip(ip):
    if not request.headers['apikey']:
            return  Response(
        "Unauthorized! You need an API token ",
        status=403,
    )
    if request.headers['apikey'] in requests:
        #print("authorized!")
        requests[request.headers['apikey']]+=1
        return jsonify(scan_local(ip))
    return  Response(
        "Unauthorized! You need an API token ",
        status=403,
    )
if __name__=="__main__":
    app.run()