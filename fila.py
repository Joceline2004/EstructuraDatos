import os
os.system('cls'if os.name == 'nt'else 'clear')
#fila en phyton
fila=[]

#añadir elementos a la fila
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
print("los elementos de la fila son:",fila)
#atender cliente (eliminar elemento de la fila)
cliente_atendido =fila.pop(0)
print("cliente atendido fue:",cliente_atendido)
print("fila despues de atender un cliente son:",fila)
