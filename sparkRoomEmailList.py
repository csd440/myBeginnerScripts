import requests
import json
import pprint
ACCESS_TOKEN='ZjFhYzI4NWMtMzViZi00MzczLTgxM2MtYzU2ZmY2MmNiMjQ5YWRjMjZjN2ItMTUz'
print("\nWe will list your most recent rooms so you may collect the room ID\nHow many of your most recent rooms would you like to list?")
maxRooms=input(": ")
URL=('https://api.ciscospark.com/v1/rooms')
HEADER={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+ACCESS_TOKEN}
PARAMS={'type':'group','max':maxRooms}
print("Retrieving your rooms, please wait")
response=requests.get(url=URL, headers=HEADER, params=PARAMS)
apiResponse=json.loads(response.text)
print(end=' ')
for n in (apiResponse['items']):
    print("\nRoom Title: "+n['title']+"\n   Room ID: "+n['id']+'\n',end=' ')
print()
print("Please enter the RoomID, not the room Title\n")
userRoomId=input(': ')
print()
URL2=('https://api.ciscospark.com/v1/memberships')
HEADER2={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+ACCESS_TOKEN}
PARAMS2={'roomId':userRoomId}
print("Retrieving members, please wait")
response2=requests.get(url=URL2, headers=HEADER2, params=PARAMS2)
apiResponse2=response2.text
for n in apiResponse2['items']:
    print (n['personEmail'])
#print(json.dumps(apiResponse, sort_keys=True, indent=1))