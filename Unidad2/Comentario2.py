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
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)
"978-84-376-9876-0": {
        "título": "Crimen y castigo",
        "autor": "Fiódor Dostoyevski",
        "géneros": ["Filosofía", "Psicología", "Novela"]
    },
    "978-84-670-0000-1": {
        "título": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "géneros": ["Fábula", "Literatura infantil", "Filosofía"]
    },
    "978-84-204-8888-4": {
        "título": "Los juegos del hambre",
        "autor": "Suzanne Collins",
        "géneros": ["Juvenil", "Aventura", "Ciencia ficción distópica"]
}