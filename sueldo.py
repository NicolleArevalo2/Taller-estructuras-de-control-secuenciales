"""
entradas
sueldo base-->float-->sueldo
venta 1-->float-->venta_1
venta 2-->float-->venta_2
venta 3-->float-->venta_3
salidas
comision-->float-->comision
"""
sueldo=float(input("Digite el sueldo base:"))
venta_1=float(input("Digite la venta_1:"))
venta_2=float(input("Digite la venta_2:"))
venta_3=float(input("Digite la venta_3:"))
comision=(((venta_1+venta_2+venta_3)/3)*0.1)
total= sueldo + comision
print("El sueldo base es:"+str(sueldo))
print("la comision del mes:"+str(comision))
print("El sueldo total del mes es:"+str(total))