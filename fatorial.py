#coding: iso-8859-1 -*-
n = int(input("Digite o valor de n:"))
calculo = n
validaN = True
if n == 0:
    calculo = 1
else:    
    while n > 2:        
        calculo = calculo * (n -1)
        n = n - 1    
print(calculo)