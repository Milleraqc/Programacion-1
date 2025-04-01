Algoritmo adivina
	Definir intento Como Entero
	Definir letra, key Como Caracter
	key <- "T"
	intento <- 0
	Escribir "Escribe la letra"
	Leer letra
	Mientras letra <> key Hacer
		intento <- intento + 1
		Escribir "Intento: ", intento, ", Ingresa de nuevo una letra"
		Leer letra
	FinMientras
	Escribir "Felicitaciones, adivinaste la letra...!!"
FinAlgoritmo
