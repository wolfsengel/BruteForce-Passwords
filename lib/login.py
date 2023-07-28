class datosImportantes:
    usuario = "Jeff Bezos" 
    password = "i<3money"
    def __private(self, usuario, password):
        self.usuario = usuario
        self.password = password

def ingresar():        
    print("Bienvenido al programa de fuerza bruta")
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    apto=False
    if usuario == datosImportantes.usuario and contrasena == datosImportantes.password:
        print("Bienvenido al sistema")
        apto=True
        #menu de acciones en el sistema
    else:  
        print("Usuario o contraseña incorrectos")

def menu():
    while True:
        print("Bienvenido al programa de fuerza bruta")
        print("1. Ingresar")
        print("2. Salir")
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            ingresar()
        elif opcion == "2":
            print("Gracias por usar el programa")
            return 0
        else:
            print("Opción incorrecta")