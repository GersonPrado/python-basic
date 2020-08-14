numero = int(input("Digite um número inteiro:"))
div = 0
i = 1
while i <=  numero:
	if numero % i == 0:
		div = div + 1
	i = i + 1

if div == 2:
	print("primo")
else:
	print("não primo")
