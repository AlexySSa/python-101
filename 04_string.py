name = "Alexy"
lastName = "Sanchez"
print(name)
print(lastName)

fullName = name + " " + lastName
print(fullName)

age = "16"
print(age)

quote = "I'm Alexy Sanchez."
print(quote)

quote2 = 'she said "hello" mari'
print(quote2)

#formato
#lo pro
template = f"Hola mi nombre es {name} y mi apellido es {lastName} mi edad es {age}."
print("v1 " + template)

#lo subnormal
#este solo agarra string, los demas combinados con los formatos
template = "hola mi nombre es " + name + " y mi apellido es " + lastName + " mi edad es " + age + "."
print("v2 " + template)

#esta forma la encuentro un poco mas enruedada
template = "hola mi nombre es {} y mi apellido es {} mi edad es {}.".format(name, lastName, age)
print("v3 " + template)