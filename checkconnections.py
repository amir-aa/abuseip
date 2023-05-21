import os,time
import threading
SLEEPTIME=50
def checkSYNFLOOD():
    while 1:
        
        os.system("netstat -tna|grep SYN| awk '{print $5}' >/tmp/connections.txt")
        with open('/tmp/connections.txt','r') as f:
            content=f.read()
            content=content.strip()
        time.sleep(SLEEPTIME)
        
if __name__=="__main__":
    t= threading.Thread(target=checkSYNFLOOD)
    t.start()