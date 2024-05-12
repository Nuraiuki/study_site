


import json
class P :
  a = int(0)
  b = str('123')

test_dict= P.__dict__
test_json = json.dumps(test_dict)
print (test_json)





