n = int(input("Digite um número inteiro:"))
somaContinua = True
calculo = 0
while somaContinua:
    calculo = calculo + (n % 10)
    n = n // 10
    if (n // 10) == 0:
        calculo = calculo + n
        somaContinua = False
print(calculo)