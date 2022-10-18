import datetime
import json
import requests


kktRegId = '0005877945061056'
token_key = '97B678C7AA750DFF0100B49C85E38C8C'
df = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
dt = datetime.datetime.now().replace(microsecond=0)
df = str(df)
dt = str(dt)
df = df.replace(" ", "%20")
dt = dt.replace(" ", "%20")
#print(kktRegId)
headers = {
    'Token': token_key,
    'Host': 'ofv-api-v0-1-1.evotor.ru',
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8',  
}
rget = 'https://ofv-api-v0-1-1.evotor.ru/v1/client/receipts?kktRegId='+kktRegId+'&dateFrom='+df+'&dateTo='+dt
print(rget)
response = requests.get(rget, headers=headers)
data = response.json()
encode_data = json.dumps(data)
decode_data = json.loads(encode_data)
if decode_data['receipts']:
    kktSum = 0
    for receipt in decode_data['receipts']:
        kktSum = kktSum + receipt['totalSum']
print(kktSum/100)
