numarul = 0
suma = 0
while((numarul % 2 == 0)or(numarul % 3 !=0)):
    nr = eval(input("dati un numar:"))
    if nr % 2 == 0:
        suma += numarul
        print(suma)