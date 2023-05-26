import mmap,json
ABUSETHRESHOLD=89
def scan_local(value):
        with open(r'badips.txt', 'rb', 0) as file:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            
            print(value)
            if s.find(value.encode()) != -1:
                return{value:'Abuseip'}
            return {value:'clean'}


def get_new_status(ip:str):
    """returns true if the abuse score is still above the Threshold otherwise False"""
    import requests

    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": True
    }
    headers = {
        "Key": "0dc7d3425e6096158be94b17c180e8046c505bc3266ad499c1f41b53970115b409f011f9033d40db",
        "Accept": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        #data=json.loads(data)

        # Process the response data as needed
        abusescore=int(data['data']['abuseConfidenceScore'])
        if abusescore> ABUSETHRESHOLD:
            return True
        return False
            



    else:
        print("Request failed with status code:", response.status_code)
        return True
     


def get_all_records():
    with open('badips.txt', 'r') as file:
        line=file.readline()
        while line !="":
             print(line)
             line=file.readline()

get_new_status('79.124.62.82')