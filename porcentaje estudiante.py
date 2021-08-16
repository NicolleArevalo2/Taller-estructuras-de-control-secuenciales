"""
entradas
numero de mujeres-->int-->numM
numero de hombres-->int-->numH
salidas
porcentaje de mujeres-->int-->porcentajeM
porcentaje de hombres-->int-->porcentajeH
"""
total=int(input("Digite el numero total de estudiantes"))
numM=int(input("Digite el numero de mujeres:"))
numH=int(input("Digite el numero de hombre"))
total=numM+numH
porcentajeM=(numM*100)/total
porcentajeH=(numH*100)/total
print("El porcentaje de mujeres es:"+str(porcentajeM))
print("El porcentaje de hombres es:"+str(porcentajeH))
