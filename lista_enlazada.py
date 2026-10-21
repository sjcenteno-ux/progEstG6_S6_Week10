def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo