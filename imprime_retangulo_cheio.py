def retangulo(l,a):
    nAltura = 0
    while nAltura < a:
        nLargura = 0
        while nLargura < l:
            print("#",end = "")
            nLargura = nLargura + 1             
        print(end = "\n")
        nAltura = nAltura + 1

l = int(input("Digite a largura:"))
a = int(input("Digite a altura:"))
retangulo(l,a)