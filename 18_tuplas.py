#no se puede cambiar los datos como lo es en el ejemplo anterior con metodos de listas, las tuplas no se puede como metodos
numbers = (1, 2, 3, 4, 5)
string = ("Alexy", "Sidor", "Pablo", "Alexy")
print(numbers)
print(type(numbers))
print("-1 => ", numbers[-1])
print("0 => ", numbers[0])

print(string)
print(type(string))

print(string.index("Pablo"))
print(string.count("Alexy"))

my_list = list(string)
print(my_list)
print(type(my_list))

my_list[1] = "Juli"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))