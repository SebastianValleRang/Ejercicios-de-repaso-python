def fibo(n):

    if(n == 0):

        return 1

    else:

        if(n == 1):

            return 1

        else:

            return n + fibo(numero-1)



n = int(input("ingrese el n termino que desea saber de fibonacci: "))

print("el n termino es de: "+str(fibo(N)))
