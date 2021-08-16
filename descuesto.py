"""
entradas
venta-->float-->venta
salidas
descuento-->float-->descuento
valor total-->float-->total
"""
venta=float(input("Digite la venta"))
descuento=(venta*0.15)
total=(venta*descuento)
print("valor de descuento:"+str(descuento))
print("Valor a pagar:"+str(total))