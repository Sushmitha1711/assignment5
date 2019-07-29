import json

data_list=[
    {"id":1001,"wname":"python","year":2019,"status":1,"company":"Heraizen"},
    {"id":1002,"wname":"ui","year":2018,"status":0,"company":"spaneos"},
    
]

try:
    with open("ws.json","w",newline='') as file:
        json.dump(data_list,file,indent=4)
       
        
except Exception as e:
    print(str(e))