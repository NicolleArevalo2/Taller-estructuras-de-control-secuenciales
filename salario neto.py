"""
entradas
horas trabajadas-->float-->horast
precio-->float-->valorh
salidas
salario base-->float-->sbase
descuento-->float-->descuento
salario neto-->float-->total
"""
horast=float(input("Digite el numero de horas trabajadas:"))
precio=float(input("Digite el valor por cada hora de trabajo:"))
sbase=horast * precio
descuento=sbase * 0.02
total=sbase - descuento
print("El salario total es:"+str(total))