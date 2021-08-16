"""
entradas
matematicas-->float-->mat
tarea 1-->float-->mat1
tarea 2-->float-->mat2
tarea 3-->float-->mat3
fisica-->float-->f
tarea 1-->float-->f1
tarea 2-->float-->f2
quimica-->float-->q
tarea 1-->float-->q1
tarea 2-->float-->q2
tarea 3-->float-->q3
salidas
promedio matematicas-->float-->promediom
promedio fisica-->float-->promediof
promedio quimica-->float-->promedioq
"""
mat=float(input("Digite la nota del examen:"))
mat1=float(input("Digite la nota tarea 1:"))
mat2=float(input("Digite la nota tarea 2:"))
mat3=float(input("Digite la nota tarea 3:"))
promediom=(mat*0.9)+(((mat1+mat2+mat3)/3)*0.1)
f=float(input("Digite la nota del examen:"))
f1=float(input("Digite la nota tarea 1:"))
f2=float(input("Digite la nota 1:"))
promediof=(f*0.8)+(((f1+f2)/2)*0.2)
q=float(input("Digite la nota del examen:"))
q1=float(input("Digite la nota tarea 1:"))
q2=float(input("Digite la nota tarea 2:"))
q3=float(input("Digite la nota tarea 3:"))
promedioq=(q*0.85)+(((q1+q2+q3)/3)*0.15)
promedio=((promediom+promediof+promedioq)/3)
print("el promedio de matematicas es:"+str(promediom))
print("el promedio de fisica es:"+str(promediof))
print("el promedio de quimica es:"+str(promedioq))