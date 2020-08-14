def remove_repetidos(lista_numeros):    
    listaSemNumeroRepetido = []
    for n in lista_numeros:
        if not n in listaSemNumeroRepetido:
            listaSemNumeroRepetido.append(n)
            
    return sorted(listaSemNumeroRepetido)
print(remove_repetidos([2,4,2,2,3,3,1]))