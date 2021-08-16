"""
entradas
n1-->int-->n1
n2-->int-->n2
n3-->int-->n3
n4-->int-->n4
n5-->int-->n5
n6-->int-->n6
n7-->int-->n7
n8-->int-->n8
salidas
total en el banco-->int-->total
"""
print("numero de billetes:")
n1=int(input("$50.000:"))
n2=int(input("$20.000:"))
n3=int(input("10.000:"))
n4=int(input("5.000:"))
n5=int(input("2.000:"))
n6=int(input("1.000:"))
n7=int(input("500:"))
n8=int(input("100:"))
total=((n1*50.000)+(n2*20.000)*(n3*10.000)+(n4*5.000)+(n5*2.000)+(n6*1.000)+(n7*5.000)+(n8*100))
print("la cantidad de dinero es:"+str(total))