import requests;

Api_url = "http://10.237.5.199:13086/SM/9/rest/devicesCMDB"
Headers =  {"Content-Type":"application/json","Authorization":"Basic Z2ZzX2ludGVncmFjaW9uOmdmc19pbnRlZ3JhY2lvbg=="}


response = requests.get(Api_url,headers=Headers)
Resp = response.json()

print("-------------------------\n")
print("Response:\n")
print("Status Code: " + str(response.status_code))

sizeColl = Resp['@count']
print(Resp['ResourceName'])

for device in range(sizeColl):
    ci = Resp['content'][device]['DevicesCMDB']['LogicalName']
    print(ci)