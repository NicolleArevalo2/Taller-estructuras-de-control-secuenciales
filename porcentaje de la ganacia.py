"""
entrada
cantidad de naranjas-->int-->X
precio por docena-->float-->YP
valor venta-->float-->K
salida
numero de decenas-->float-->nd
precio-->float-->p
ganacias-->float-->g
porcentaje de las ganancias-->float-->porcentaje
"""
X=int(input("digite el numero de naranjas:"))
YP=float(input("digite el precio por decena:"))
K=float(input("digite el valor de las ventas:"))
nd=(X/12)
p=(YP*nd)
g=(p-K)
porcentaje=((g*100)/p)
print("el porcenaje de ganancias es:"+str(porcentaje),"%")