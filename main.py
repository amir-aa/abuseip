from flask import Flask,jsonify
from token_1 import *
app=Flask()

@app.route('/token')
def token():

    return jsonify({'key':generate_api_key()})
@app.route('/checkip/<ip>')
def checkip(ip):
    
if __name__=="__main__":
    app.run()