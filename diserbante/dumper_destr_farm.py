import requests
import sys

host = sys.argv[1]

if(len(sys.argv)> 2):
    tulip_host = sys.argv[2]
else:
    tulip_host = host

url_api = f"http://{tulip_host}:3000/api/"
headers = {'Content-Type': 'application/json'}

#metti ip di destr farm
data = {"dst_port":5001, "includeTags":["flag-in"]}

print(data)

def get_flow(oid):
    res = requests.get(url_api + "flow/" + oid).json()

    return res

response = requests.post(url_api + "query", headers=headers, json=data).json()

oids = list(map(lambda x : x['_id']['$oid'], response))

for oid in oids[:5]:
    print(get_flow(oid), flush=True)
