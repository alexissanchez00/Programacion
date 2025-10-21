
def guardar_libro(titulo, autor):
    with open("libros.txt", "a", encoding="utf-8") as f:
        f.write(f"{titulo},{autor}\n")
    print(f" Libro '{titulo}' guardado correctamente.")
