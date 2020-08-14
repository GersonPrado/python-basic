def inverte_lista(lista_numero):
    tamanho = len(lista_numero) - 1
    while tamanho > 0:
        print(lista_numero[tamanho -1])
        tamanho = tamanho - 1

numero = 1
lista = []

while numero != 0:
    numero = int(input("Digite um número: "))
    lista.append(numero)

inverte_lista(lista)