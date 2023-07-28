import sys
import os
import login
import time

def read_passwords(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]
    
def try_password(password):
    return ingresar(password)

def ingresar(password):
    usuario = "Jeff Bezos"
    contrasena = password
    apto=False
    if usuario == login.datosImportantes.usuario and login.datosImportantes.password == login.datosImportantes.password:
        print("Bienvenido al sistema")
        apto=True
        return apto
        #menu de acciones en el sistema
    else:  
        print("Usuario o contraseña incorrectos")
        
start = time.time()

for password in read_passwords("merged.txt"):
    
    try_password(password)
    
end = time.time()
total = end - start
print(f"Tiempo total: {total}")
if total > 60:
    print("Tiempo excedido")
    sys.exit(0)
