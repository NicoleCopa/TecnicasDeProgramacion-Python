Algoritmo ejercicio10
	Definir minutos, minutosSobrantes Como Entero
	Definir horas Como Real
	
	Escribir "Ingrese la cantidad de minutos a convertir:";
	Leer minutos;
	
	horas <- redon(minutos / 60);
	
	minutosSobrantes <- minutos % 60;
	
	Escribir "La cantidad ingresada corresponde a ", horas, " horas y ", minutosSobrantes, " minutos";
FinAlgoritmo
