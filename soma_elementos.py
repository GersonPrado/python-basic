def soma_elementos(lista_numero):
    somaNumeros=0
    for n in lista_numero:
        somaNumeros = somaNumeros + n
    return somaNumeros

print(soma_elementos([2,4,2,33,2]))