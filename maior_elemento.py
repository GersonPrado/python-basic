def maior_elemento(lista_numeros):
    maiorNumero = lista_numeros[0]
    for n in lista_numeros:         
        if n > maiorNumero:
            maiorNumero = n
    return maiorNumero
print(maior_elemento([-90,-27,-12]))