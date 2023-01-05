person = {
  "name": "Alexy",
  "last_name": "Sanchez",
  "age": 16,
  "city": "San Salvador",
  "langs": ["python", "php", "java"],
}

print(person)
print("**************")

person["name"] = "Ariel"
person["age"] -= 12
person["langs"].append("C++")
print(person)
print("**************")

del person["city"]
person.pop("age")
print(person)
print("**************")
#tuplas
print("items")
print(person.items())
#solo las keys
print("keys")
print(person.keys())
#solo los valores de las keys
print("values")
print(person.values())