import json
f = open("C:/Users/TaaAbu/PycharmProjects/sample/tt/.json")
j_data = json.load(f)
print (j_data["emp2"]["name"])