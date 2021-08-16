"""
entrada
precio final-->float-->pf
precio de venta-->float-->pv
salida
porcentaje de descuento-->float-->descuento
diferencia-->float-->dif
"""
pf=float(input("digite el valor pagado:"))
pv=float(input("digite el precio de venta:"))
dif=(pf - pv)
descuento=(dif*100)/pf
print("el porcentaje de descuento fue:"+str(descuento))