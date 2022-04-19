from sys import argv, exit
from socket import setdefaulttimeout, socket, gethostbyname, SOCK_STREAM, AF_INET
from concurrent.futures import ThreadPoolExecutor

def t(i):
    target = i.split(":")[0]
    port = 23

    s = socket(AF_INET, SOCK_STREAM)
    setdefaulttimeout(3)
         
    result = s.connect_ex((target,port))
    
    if result == 0:
        print(i.replace("\n", ""))
        
    s.close()
    
    
for i in open(argv[1], "r").readlines():
    ThreadPoolExecutor(max_workers=40).submit(t, i)
