a=1


while(True):
    
    for i in range(20):

        print(str(a)+" ",end="")
        a =a+1

    if(a == 1001):

        print("Lista completada")
        break

    cof = input("\n Escriba 1 si desea continuar o 2 si desea detenerlo\n")

    if(cof == 1):

        break
