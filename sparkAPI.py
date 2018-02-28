import requests
import json
ACCESS_TOKEN='YOU TOKEN'
apiReference=('rooms','Memberships','Messages','Teams','Team Memberships','Webhooks','Organizations','Licenses','Roles','Events')
print("Type in the API Call you wish to make, please note items are case sensitive:\n",end=' ')
for i in apiReference:
    print(i+',', end=' ')
userAPI=input('\n:')
print("Please wait:")
URL=('https://api.ciscospark.com/v1/'+userAPI)
HEADER={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+ACCESS_TOKEN}
PARAMS={'type':'group','max':'2'}
response=requests.get(url=URL, headers=HEADER, params=PARAMS)
print("Your base API Call will go here\n"+URL)
print("Your Spark Developer Token: "+HEADER['Authorization'])
print('\n\n')
print(response.status_code)
apiResponse=json.loads(response.text)
print('key:',end=' ')
returnedVal1=(apiResponse['items'])
for n in returnedVal1[0]:
    print(str(n), end=' ')
    for z in returnedVal1[0][n]:
       print(str(z), end=' ')
