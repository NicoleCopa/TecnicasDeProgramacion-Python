"""Se requiere un algoritmo que calcule el sueldo neto de un trabajador. Para ello, 
el algoritmo debe admitir el ingreso del monto a cobrar por horas, el total de 
horas trabajadas y a este total le debe restar las cargas sociales y aportes (17%)"""

print("""-------------------------------------------------------
                EJERCICIO 13: SUELDO NETO
-------------------------------------------------------""")

monto_por_hora = float(input("Ingrese el monto a cobrar por horas: "))
horas_trabajadas = int(input("Ingrese el total de horas trabajadas: "))

sueldo_bruto = monto_por_hora * horas_trabajadas
sueldo_neto = sueldo_bruto - (sueldo_bruto * 0.17)

print(f"Su sueldo neto es: ${sueldo_neto}")