text = "Ella sabe python"
print(text[0])
print(text[1])
#print(text[99])

size = len(text)
print("longitud =>", size)
print(text[size - 1])
print(text[-1])

#slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:])
print(text[:])
print(text[10:16:1])
print(text[10:16:2]) #esto salta uno y pone lo otro
print(text[::2])