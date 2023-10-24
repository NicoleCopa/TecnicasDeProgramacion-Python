Algoritmo ejercicio13
	Definir monto_por_hora, sueldo_bruto, sueldo_neto Como Real
	Definir horas_trabajadas Como Entero
	
	Escribir "Ingrese el monto a cobrar por horas:";
	Leer monto_por_hora;
	
	Escribir "Ingrese el total de horas trabajadas:";
	Leer horas_trabajadas;
	
	sueldo_bruto <- monto_por_hora * horas_trabajadas;
	
	sueldo_neto <- sueldo_bruto - (sueldo_bruto * 0.17);
	
	Escribir "Su sueldo neto es: $", sueldo_neto;
FinAlgoritmo
