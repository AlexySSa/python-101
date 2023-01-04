user_opcion = input("piedra, papel o tijeras => ")
user_opcion = user_opcion.lower()
PC_opcion = ("papel")
print(PC_opcion)

if(user_opcion == PC_opcion):
  print("este es un empate")
  
elif user_opcion == "piedra":
  if PC_opcion == "tijeras":
    print("piedra gana a tijeras")
    print("user gano")
  else:
   print("papel gana a piedra")
   print("pc gano")
elif user_opcion == "papel":
  if PC_opcion == "piedra":
    print("papel gana a piedra")
    print("user gano")
  else:
    print("tijeras gana a papel ")
    print("pc gano")
elif user_opcion == "tijeras":
  if PC_opcion == "papel":
    print("tijeras gana a papel")
    print("user gano")
  else:
    print("piedra gana a tijeras")
    print("pc gano")
  
