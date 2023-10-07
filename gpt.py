import pyperclip

texto = open("texto.txt", encoding="utf8").read()
texto = " ".join(texto.split()) #Elimina espacios innecesarios

size = 4096
conjuntos = []

for i in range(0, len(texto), size):
    conjunto = texto[i:i+size]
    conjuntos.append(conjunto)

while conjuntos:
    data = conjuntos.pop(0)
    pyperclip.copy(data)
    input(data)