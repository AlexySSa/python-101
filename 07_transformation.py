name = "Alexy"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))
#los print necesitan tener siempre el mismo tipo de dato
print("Alexy " + "Sanchez")
print(10 + 20)

age = 12
#aqui tranformamos un int a str, re easy xd 
print("mi edad es " + str(age))
#este tambien transforma automaticamente 
print(f"mi edad es {age}" )

age = input("Ingresa tu edad: ")
print(type(age))
age = int(age)
print(type(age))
print(f"tu edad en 10 año sera {age + 10}")