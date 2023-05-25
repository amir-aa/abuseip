import os,time
import threading
from collections import Counter
SLEEPTIME=50
def checkSYNFLOOD():
    while 1:
        
        os.system("netstat -tna|grep SYN| awk '{print $5}' >/tmp/connections.txt")
        with open('/tmp/connections.txt','r') as f:
            content=f.readlines()
            maliciouslist=[k for k,v in Counter(content).items() if v>3]
            print(maliciouslist)
            
        time.sleep(SLEEPTIME)
        
if __name__=="__main__":
    t= threading.Thread(target=checkSYNFLOOD)
    t.start()