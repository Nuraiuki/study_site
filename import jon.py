import json

data=[1,2,3,'4','6','fvd','fvgr',True]

with open ('data.json','w') as json_file:
    json.dump(data,json_file)



