#CRUD create, read, update & delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers) 

#aqui se agrega un elemneto al final de la lista
#puedes agregar cualquier tipo sea int o str
numbers.append(700)
print(numbers)

#primero se pone en que posicion y despues lo que se inserta
numbers.insert(0, "hola")
print(numbers)

numbers.insert(4, "un paso a la derecha")
print(numbers)

tasks = ["todo 1", "todo 2", "todo 3"]

new_list = numbers + tasks
print(new_list)

index = new_list.index("todo 2")
new_list[index] = "change"
print(new_list)

new_list.remove("todo 1")
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

#sort no puede mezclar tipo de datos
numbers_a = [1, 5, 3, 6, 9]
numbers_a.sort()
print(numbers_a)

string = ["a", "re", "vd", "ab", "bf"]
string.sort()
print(string)

'''

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

'''