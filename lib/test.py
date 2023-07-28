import time

start_time = time.time()

#Buscar una palbara en la lista merged.txt
#introduce palabra a buscar
palabra = input("Introduce la palabra a buscar: ")
t=0
i=0
p=0
with open("merged.txt", "r") as file:
    for line in file:
        #si empieza con la palabra
        if palabra in line and line.startswith(palabra):
            print("Palabra encontrada:", line)
            p=p+1
        else:
            if palabra in line:
                print("Palabra encontrada:", line)
                i=i+1
t=i+p
print("Palabras encontradas al inicio:", p)
print("Palabras encontradas:", t)
print("Tiempo transcurrido:", time.time() - start_time, "segundos")