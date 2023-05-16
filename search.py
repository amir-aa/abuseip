import mmap
def scan_local(value):
        with open(r'.\\hashdb.txt', 'rb', 0) as file:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            
            print(value)
            if s.find(value.encode()) != -1:
                return{value:'Abuseip'}
            return {value:'clean'}
