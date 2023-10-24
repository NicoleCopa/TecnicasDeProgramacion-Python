Algoritmo ejercicio20
	Definir num1, num2, num3 Como Entero
	
	Escribir "Ingrese un número:";
	Leer num1;
	Escribir "Ingrese otro número:";
	Leer num2;
	Escribir "Ingrese otro número:";
	Leer num3;
	
	Si (num1 > num2) Y (num1 > num3) Entonces
		Escribir "El número ", num1, " es mayor";
	SiNo Si (num2 > num3) Entonces
			Escribir "El número ", num2, " es mayor";
		SiNo
			Escribir "El número ", num3, " es mayor";
		FinSi
	FinSi
FinAlgoritmo