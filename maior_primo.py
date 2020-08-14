def maior_primo(x):
    y = 1
    ultimo_primo = 0
    while y <= x:
        if en_numero_primo(y):
            ultimo_primo = y
        y = y +1    
    return ultimo_primo

def en_numero_primo(numero):
    div = 0
    i = 1
    while i <=  numero:
        if numero % i == 0:
            div = div + 1
        i = i + 1
    if div == 2:
        return True
    else:
        return False
    
