Algoritmo ejercicio17
	Definir num, num_impar Como Entero
	
	Escribir "Ingrese un número:";
	Leer num
	
	Si num MOD 2 <> 0 Entonces
		num_impar <- num * 2
		Escribir num, " x 2 = ", num_impar;
	FinSi
	
FinAlgoritmo