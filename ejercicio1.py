x=int(input("ingrese un tiempo en segundos: "))
z=print ("¿cuanto tiempo toma en terminar una tarea? ")

a=int(input("ingrese la hora: "))
b=int(input("ingrese los minutos: "))
c=int(input("ingrese los segundos: "))

k= a*3600
r= b*60
s= c*1

t= k+r+s
if(t<=x):
     print(" si alcanza el tiempo para acabar la tarea")
if(t>x):
     print(" no alcanza el tiempo para acabar la tarea")
     