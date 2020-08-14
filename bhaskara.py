import math
a = float(input("Digite o valor da constante a:"))
b = float(input("Digite o valor da constante b:"))
c = float(input("Digite o valor da constante c:"))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raizDelta = math.sqrt(delta) 
    xLinha1 = ((-b + raizDelta) / (2*a))
    if delta == 0:
        print("a raiz desta equação é", xLinha1)
    else:
        xLinha2 = ((-b - raizDelta) / (2*a))
        if xLinha1 < xLinha2:
            print("as raízes da equação são", xLinha1,"e",xLinha2)        
        else:
            print("as raízes da equação são", xLinha2,"e",xLinha1)
