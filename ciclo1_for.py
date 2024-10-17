numero1 = input("Ingrese el nùmero de la tabla: ") #ingreso de la variable por el usuario 
numero1 = int(numero1) # Convierte la entrada a un entero
print (f"La tabla de multiplicar del numero {numero1}  es: ")
for i in range(1, 11): # ciclo for inicia del 1 al 10 
    resultado = numero1 * i 
    print(f"{numero1} x {i} = {resultado}")