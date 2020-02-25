import random

matriz=[]

for i in range(3):

    matriz.append([0]*4)

for i in range(0,3):
    for j in range(0,4):

        matriz[i][j]=random.randint(1,20)

print("La matriz inicial es: ") 
print(matriz)

for i in range(0,3):
    for j in range(0,4):

        if( i == 2 and j == 2):

            print("el numero en la posicion 2,2 es: ")
            print(matriz[i][j])           

        else:

            matriz[i][j] = (matriz[i][j])/(matriz[2][2])
            
print("La matriz con sus divisiones es: ")             
print(matriz)
    
