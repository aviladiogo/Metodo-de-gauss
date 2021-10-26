def preencheMatriz():
    x = 0
    y = 0
    while y < LinhasT:
        while x < ColunasT:
            Sistema[y,x] = int(input("insira o valor na linha " + str(y) + ", Coluna " + str(x) +": "))
            x+=1
        x = 0
        y += 1

def Gauss(linha, coluna):
    linha1 = linha+1
    cont = 0
    while cont <= LinhasT-1:
        M = Sistema[linha1,coluna] / Sistema[linha,coluna]
        x=0 
        while x <= ColunasT-1:
            Sistema[linha1,x] = Sistema[linha1,x] - M * Sistema[linha,x]
            Sistema[linha1,x] = round(Sistema[linha1,x], 2)
            x+=1
        if linha1 + 1 != tamanho:
            linha1 += 1
        print(Sistema)
        print("")
        cont += 1
    
    if linha + 1 != tamanho-1:
        Gauss(linha+1, coluna +1)
    

import numpy as np

tamanho = int(input("insira o tamanho do sistema linear: "))
ColunasT = tamanho 
LinhasT = tamanho
Sistema = np.zeros((LinhasT,ColunasT), float) 
preencheMatriz()
print(Sistema)
print("")
linha = 0
coluna = 0
Gauss(linha, coluna)