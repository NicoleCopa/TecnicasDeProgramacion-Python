"""Se requiere un algoritmo que calcule el monto a abonar por el servicio de luz eléctrica.
Para ello, se deberá ingresar el valor anterior del medidor y el valor actual seguidamente
se deberá calcular el total de la factura mensual, considerando que cada Kw cuesta $125.60."""

print("""-------------------------------------------------------
                EJERCICIO 12: LUZ ELÉCTRICA
-------------------------------------------------------""")

valor_anterior = float(input("Ingrese el valor anterior del medidor en Kw: "))
valor_actual = float(input("Ingrese el valor actual del medidor en Kw: "))

consumo = valor_actual - valor_anterior

valor_por_kw = 125.60

monto_abonar = consumo * valor_por_kw

print(f"El monto a abonar por el servicio de luz es de ${monto_abonar}")