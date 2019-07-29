data_list=[
    {"id":1001,"wname":"python","year":2019,"status":1,"company":"Heraizen"},
    {"id":1002,"wname":"ui","year":2018,"status":0,"company":"spaneos"},
    
]

try:
    with open("ws.txt","w") as file:
        for d in data_list:
            line=f'{d["id"]},{d["wname"]},{d["year"]},{d["status"]},{d["company"]}\n'
            file.write(line)

except Exception as e:
    print(str(e))