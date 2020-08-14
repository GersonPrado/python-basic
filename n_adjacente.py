numeroDigitado = input("Digite um número inteiro:")
tamanhoNumeroDigitado = len(numeroDigitado)
numero = int(numeroDigitado)
numeroPosicao = 0
i = 1
numeroAdjacente = False

while i < tamanhoNumeroDigitado and not numeroAdjacente:
    numeroPosicao = numero % 10
    numero = numero // 10
    if numeroPosicao == numero % 10:
        numeroAdjacente = True
    i = i + 1

if numeroAdjacente:
		print("sim")
else:
		print("não")