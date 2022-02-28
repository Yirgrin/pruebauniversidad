
print ("Ingrese las horas laboradas durante la semana")
semanales = int (input())

print ("Ingrese el monto que recibe por cada hora laborada")
preciohora = int (input())

salario = preciohora * semanales 
jornada = 48

if semanales>jornada: 
    extrasemanales = (semanales - jornada) * preciohora
    salarioextra = salario + extrasemanales
    print ("Su salario es semanal es de" , salarioextra)
else: 
    print ("Su salario es semanal es de" , salario)