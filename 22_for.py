'''

for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ("Juli", "Alexy", "Piedra")
for element in my_tuple:
  print(element)

person = {
  "name": "camisa",
  "price": 100,
  "stock": 89
}
for key in person:
  print(key, "=>", person[key])

for key, value in person.items():
  print(key, "=>", value)

people = [
  {
    "name": "Nico",
    "age": 34
  },
  {
    "name": "Alexy",
    "age": 16
  },
  {
    "name": "Santi",
    "age": 12
  }
]

for person in people:
  print("name =>",person["name"])