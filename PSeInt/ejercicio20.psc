Algoritmo ejercicio20
	Definir num1, num2, num3 Como Entero
	
	Escribir "Ingrese un n�mero:";
	Leer num1;
	Escribir "Ingrese otro n�mero:";
	Leer num2;
	Escribir "Ingrese otro n�mero:";
	Leer num3;
	
	Si (num1 > num2) Y (num1 > num3) Entonces
		Escribir "El n�mero ", num1, " es mayor";
	SiNo Si (num2 > num3) Entonces
			Escribir "El n�mero ", num2, " es mayor";
		SiNo
			Escribir "El n�mero ", num3, " es mayor";
		FinSi
	FinSi
FinAlgoritmo