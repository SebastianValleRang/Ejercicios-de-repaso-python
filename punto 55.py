import random

matriz=[]

acumulador = 0

for i in range(3):

    matriz.append([0]*3)

for i in range(0,3):
    for j in range(0,3):

        matriz[i][j]=random.randint(1,20)

        if(j > i):

            acumulador = matriz[i][j]+acumulador


print(acumulador)
print(matriz)
    
