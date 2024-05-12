import json

listmy=[1,2,3,'4','6','fvd','fvgr',True]

with open ('listm.json','w') as json_file:
    json.dump(listmy,json_file)

with open ('listm.json','r') as json_file:
    loaded=json.load(json_file)

print(loaded)


import pickle 


fruits={
    'apple':5,
    'banana':6,
    'cherry':4
}

with open ('fruit_data.pkl','wb') as pickle_file:
    pickle.dump(fruits,pickle_file)

with open ('fruit_data.pkl','rb') as pickle_file:
    loadr=pickle.load(pickle_file)
print(loadr)
