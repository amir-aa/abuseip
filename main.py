from flask import Flask,jsonify,request
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
    if request.headers['apikey'] in requests:
        print("authorized!")
        requests[request.headers['apikey']]+=1
    return jsonify(scan_local(ip))
if __name__=="__main__":
    app.run()