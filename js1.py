import json


try:
    with open("ws.json","r") as file:
        data_list=json.load(file)
        for w in data_list:
            print(f"ID:{w['id']} Name:{w['wname']} Year:{w['year']} Status:{w['status']} Company:{w['company']}")
        
        
except Exception as e:
    print(str(e))