import requests
import sys

host = sys.argv[1]

url_api = f"http://{host}:3000/api/"
headers = {'Content-Type': 'application/json'}
data = {"service":"","includeTags":["flag-in"]}

def get_flow(oid):
    res = requests.get(url_api + "flow/" + oid).json()

    return res

response = requests.post(url_api + "query", headers=headers, json=data).json()

oids = list(map(lambda x : x['_id']['$oid'], response))

for oid in oids[:5]:
    print(get_flow(oid), flush=True)
