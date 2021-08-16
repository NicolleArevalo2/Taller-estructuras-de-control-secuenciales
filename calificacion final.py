"""
entradas
calificacion1-->float-->c1
calificacion2-->float-->c2
calificacion3-->float-->c3
examen final-->float-->examen_final
trabajo final-->float-->trabajo_final
salidas
promedio-->float-->promedio
nota definitiva-->float-->total
"""
c1=float(input("Digite calificacion 1:"))
c2=float(input("Digite calificacion 2:"))
c3=float(input("Digite calificacion 3:"))
promedio= (c1+c2+c3)/3
examen_final=float(input("Digite nota del examen final:"))
trabajo_final=float(input("Digite la calificaion del trabajo final:"))
total= (promedio*0.55) + (examen_final*0.3) + (trabajo_final*0.15)
print("El promedio final de la materia de programacion es:"+str(total))