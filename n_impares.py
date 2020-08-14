#coding: iso-8859-1 -*-
n = int(input("Digite o valor de n:"))
i = 0
calculo = 1
while i < n:
    if calculo % 2 == 1:
        print(calculo)
        i = i + 1
    calculo = calculo + 1
