import random

opcions = ("piedra", "papel", "tijeras")

user_opcion = input("piedra, papel o tijeras => ")
user_opcion = user_opcion.lower()

if not user_opcion in opcions:
  print("la opcion que eligiste nada que ver por que es ", user_opcion)
  exit()
  
PC_opcion = (random.choice(opcions))

print("user opcion => ", user_opcion)
print("PC opcion => ",PC_opcion)

if(user_opcion == PC_opcion):
  print("este es un empate")
  
elif user_opcion == "piedra":
  if PC_opcion == "tijeras":
    print("piedra gana a tijeras")
    print("user gano")
  else:
   print("papel gana a piedra")
   print("PC gano")
elif user_opcion == "papel":
  if PC_opcion == "piedra":
    print("papel gana a piedra")
    print("user gano")
  else:
    print("tijeras gana a papel ")
    print("PC gano")
elif user_opcion == "tijeras":
  if PC_opcion == "papel":
    print("tijeras gana a papel")
    print("user gano")
  else:
    print("piedra gana a tijeras")
    print("PC gano")
  
