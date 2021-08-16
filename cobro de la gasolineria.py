"""
entrada
venta en galones-->float-->g
salida
venta en litros-->float-->l
total-->float-->total
"""
g=float(input("digite la venta en galones:"))
l=(g * 50.000)
total=(l *3.785)
print("el total de la venta es:"+str(total))