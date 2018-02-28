import requests
import json
apiReference=('rooms','Memberships','Messages','Teams','Team Memberships','Webhooks','Organizations','Licenses','Roles','Events')
print("Type in the API Call you wish to make, please note items are case sensitive:\n",end=' ')
for i in apiReference:
    print(i+',', end=' ')
userAPI=input('\n:')
ACCESS_TOKEN='ZjFhYzI4NWMtMzViZi00MzczLTgxM2MtYzU2ZmY2MmNiMjQ5YWRjMjZjN2ItMTUz'
URL=('https://api.ciscospark.com/v1/'+userAPI)
HEADER={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+ACCESS_TOKEN}
PARAMS={'type':'group','max':'2'}
response=requests.get(url=URL, headers=HEADER, params=PARAMS)
print("Your base API Call will go here\n"+URL)
print("Your Spark Developer Token: "+HEADER['Authorization'])
print('\n\n')
print(response.status_code)
apiResponse=json.loads(response.text)
print(apiResponse['items'])
for e in apiResponse['items'][0]['id']:
    print(e)
