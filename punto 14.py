a = input("ingrese la coordenada x1: ")
b = input("ingrese la coordenada x2: ")
c = input("ingrese la coordenada y1: ")
d = input("ingrese la coordenada y2: ")

e = float(a)
f = float(b)
g = float(c)
h = float(d)

opx1 = e-f
opx2 = f-e
opy1 = g-h
opy2 = h-g

x = 0
y = 0

if opx1 > 0:
    x =  opx1
else:
    x =  opx2

if opy1 > 0:
    y = opy1
else:
    y = opy2

resultado = x*y

print("el area del rectangulo es de: "+str(resultado))

        
