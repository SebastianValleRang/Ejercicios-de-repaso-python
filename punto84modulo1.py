from punto84modulo2 import *

pcadena = str(input("Ingrese el primer numero octal: "))
scadena = str(input("Ingrese el segundo numero octal: "))

a = ConvertirOctDeci(pcadena)
b = ConvertirOctDeci(pcadena)

print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,b))
