def retangulo(l,a):
    nAltura = 2
    imprimeLinha(False,l)
    
    while nAltura < a :
        nLargura = 0
        imprimeLinha(True,l)        
        nAltura = nAltura + 1
    
    imprimeLinha(False,l)
    
def imprimeLinha(vazada, l):
    if vazada:
        nLinha = 2
        print("#",end ="")
        while nLinha < l:
            print(end = " ")
            nLinha = nLinha + 1
        print("#")
    else:
        nLinha = 0        
        while nLinha < l:
            print("#", end = "")
            nLinha = nLinha + 1        
        print(end="\n")
l = int(input("Digite a largura:"))
a = int(input("Digite a altura:"))
retangulo(l,a)