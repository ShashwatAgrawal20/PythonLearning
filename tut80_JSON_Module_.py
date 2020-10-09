# JSON - Javascript object notation.... ((Fullform of Json))
import json

# print(dir(json))
data = '{"var1":"Shashwat", "var2":"Saransh"}'
# agr aapan ne ye kiya to ye nhi honga kyuki ye intergere nhi hai ..  
# print(data['var1'])
parse = json.loads(data)
# aur agr iss ko jason me kiya to ye ho jayenga.
print(parse['var1'])
print(type(parse))



data2 = {
    "cars":['bmw', 'audi', 'ferrari'],
    "fridge":('roti', 'tatti'), 
    "isbad":False
}
# iss ko  aaapn java script me bhi convert kr skte hai .

jsonss = json.dumps(data2)
print(jsonss)
