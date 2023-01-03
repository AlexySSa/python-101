text = "Ella sabe programar en Python"

'''

print("javaScript" in text)
print("python" in text)

if "python" in text:
    print("Python is a good programming language")
else:
    print("tambien eligiste bien")

'''

size = len("amor")
print(size)
print(text)
print(text.upper())
print(text.lower())
print(text.count("a"))

print(text.swapcase())
print(text.startswith("Ella"))
print(text.endswith("Python"))
print(text.replace("Python", "Go"))

text2 = "este es un titulo"

print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
print("234".isdigit())