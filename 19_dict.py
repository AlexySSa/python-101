my_dict = {}
print(type(my_dict))

my_dict = {
  "Avion": "bla bla bla",
  "Name": "Alexy Sanchez",
  "Age": 16,
  "City": "San Salvador",
}

print(my_dict)
print(len(my_dict))

print(my_dict["Avion"])
print(my_dict["Age"])

#get ayuda mucho como sabe manejar si no hay ningun valor y con esto el proceso sigue funcionando si ningu problema
print(my_dict.get("unvalor"))

#tambien ayuda el in para comprobar si existe un valor
print("Avion" in my_dict)
print("QuienSos" in my_dict)