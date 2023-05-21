from asgiref.wsgi import WsgiToAsgi
from flask import Flask,jsonify,request,Response
import os
from token_1 import *
from search import *
app=Flask(__name__)
asgi_app = WsgiToAsgi(app)
LIMIT=4

requests={}
def checksingleip(ip:str):
    os.system('curl -G https://api.abuseipdb.com/api/v2/check  --data-urlencode "ipAddress={}" -d maxAgeInDays=90  -H "Key: 0dc7d3425e6096158be94b17c180e8046c505bc3266ad499c1f41b53970115b409f011f9033d40db" -H "Accept: application/json"'.format(ip))
    
@app.route('/token')
def token():
    k=generate_api_key()
    requests[k]=0
    GetLog(request.remote_addr,k)
    return jsonify({'key':k})
@app.route('/checkip/<ip>')
def checkip(ip):
    try:
        if request.headers['apikey'] in requests:
            
            requests[request.headers['apikey']]+=1
            if int(requests[request.headers['apikey']])>LIMIT:
                return Response ("limit Exceeded! please take another token!",status=403)
            return jsonify(scan_local(ip))
        return  Response(
            "Unauthorized! You need an API token ",
            status=403,
        )
    except KeyError:
        return  Response(
            "Unauthorized! You need an API token ",
            status=403,
        )
    except Exception as ex:
        return jsonify({'UnknownError':str(ex)})

if __name__=="__main__":
    app.run()