numero1 = int(input("Recebe o primeiro número:")) 
numero2 = int(input("Recebe o segundo número:")) 
numero3 = int(input("Recebe o terceiro número:")) 

if numero1 > numero2:
    print("não está em ordem crescente")
else:
    if(numero2 > numero3):
        print("não está em ordem crescente")
    else:
        print("crescente")   