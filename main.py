from asgiref.wsgi import WsgiToAsgi
from flask import Flask,jsonify,request,Response
from token_1 import *
from search import *
app=Flask(__name__)
asgi_app = WsgiToAsgi(app)
LIMIT=4
requests={}
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