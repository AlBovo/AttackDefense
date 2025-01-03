import requests

# va migliorato

for i in range(0, 88):
    host = f"10.60.{i}.1"

    print("Trying: ", host)

    try:
        rep = requests.get("http://" + host + ":3000/api")
        if(rep.status_code == 200):
            print(rep.text)
            if(rep.text == "Hello, World!"):
                print(f"Found Tulip at {host}")
    except:
        continue
