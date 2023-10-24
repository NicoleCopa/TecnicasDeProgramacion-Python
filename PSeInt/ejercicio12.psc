Algoritmo ejercicio12
	Definir valor_anterior, valor_actual, consumo, valor_por_kw, monto_abonar Como Real
	
	Escribir "Ingrese el valor anterior del medidor en Kw:";
	Leer valor_anterior
	
	Escribir "Ingrese el valor actual del medidor en Kw:";
	Leer valor_actual;
	
	consumo <- valor_actual - valor_anterior
	
	valor_por_kw <- 125.60
	
	monto_abonar <- consumo * valor_por_kw
	
	Escribir "El monto a abonar por el servicio de luz es de $", monto_abonar;
FinAlgoritmo
