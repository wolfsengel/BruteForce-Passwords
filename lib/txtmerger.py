import os

pathy = "./assets/outpost9.com/"

def merge_txt_files(pathy):
    """
    Merge all text files in a directory into a single file.
    """
    with open("./assets/outpost9.com/merged.txt", "w") as merged_file:
        for file_name in os.listdir(pathy):
            if file_name.endswith(".txt"):
                print(f"Uniendo {file_name}...")
                file_path = os.path.join(pathy, file_name)
                try:
                    with open(file_path, "r") as file:
                        merged_file.write(file.read() + "\n")
                        print(f"Archivo {file_name} unido exitosamente.")
                except Exception as e:
                    print(f"Error al leer el archivo {file_path}: {str(e)}")

merge_txt_files(pathy)
