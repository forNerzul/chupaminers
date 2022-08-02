#Fuente de INFO IMPORTANTISIMA!! 
# https://www.instructables.com/Netcat-in-Python/
# https://thomassileo.name/blog/2013/09/17/playing-with-python-and-cgminer-rpc-api/


import socket
import time
import json

miner_ip = "192.168.44.50"
port = 4028
farm_proxy_pool = "stratum2+tcp://192.168.10.222/u95GEReVMjK6k5YqiSFNqqTnKU4ypU2Wm8awa6tmbmDmk1bWt"

def netcat (miner_ip,port,content):
    # initialize the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((miner_ip,port))

    sock.sendall(content)
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()


    print("Connection closed.")
    sock.close()
    res_as_json = json.loads(res[:-1])
    return res_as_json

content = '{"command":"addpool stratum2+tcp://192.168.10.222/u95GEReVMjK6k5YqiSFNqqTnKU4ypU2Wm8awa6tmbmDmk1bWt\,penguindigital.16x214\,123"}'

cosito = netcat(miner_ip, port, content.encode())

print("-------------------------------------------------------")

# print(cosito["POOLS"][0]["URL"])
print(cosito)
print(f"Type of Response: {type(cosito)}")



