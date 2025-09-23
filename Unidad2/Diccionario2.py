import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
        "978-84-670-4952-2": {
        "título": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "géneros": ["Misterio", "Drama", "Ficción histórica"]
    },
    "978-84-376-0493-0": {
        "título": "Pedro Páramo",
        "autor": "Juan Rulfo",
        "géneros": ["Realismo mágico", "Novela corta"]
    },
    "978-84-204-6837-7": {
        "título": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez",
        "géneros": ["Romance", "Realismo mágico"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:",info_libro)