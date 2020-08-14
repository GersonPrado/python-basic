import math

x1 = int(input("Receba x1:"))
y1 = int(input("Receba y1:"))
x2 = int(input("Receba x2:"))
y2 = int(input("Receba y2:"))

ponto1 = (x1 - x2) ** 2
ponto2 = (y1 - y2) ** 2
distancia = math.sqrt(ponto1 + ponto2)
if distancia < 10:
    print("perto")
else:
    print("longe")    