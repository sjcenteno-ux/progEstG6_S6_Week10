#Esto es para crear el nodo, por ejemplo seria: ingrese el siguiente en la fila: santiago, se agregaria en dato santiago y en siguiente none. 
def crearNodo(dato):
    return {"dato": dato, "siguiente": None}

#reutilizamos la funcion anterior para crear un nuevo nodo, luego usamos nuevo["siguiente"] = cabeza, para que se conecte con la cabeza anterior 
def insertarInicio(cabeza, dato):
    nuevo = crearNodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo 

#si la cabeza esta vacia, no entraria al while porque no hay nodos en la lista enlazada y la cabeza seria el nuevo nodo que acabamos de crear.
#definimos actual= cabeza para recorrer con un while la lista con elementos y si el siguiente no es None, actual cambia al siguiente, cuando se rompa el while.
#actual["siguiente"] en vez de none, sera el nuevo y el nuevo lleva el dato y siguiente: None, asi no rompe la logica y se returna la cabeza, porque se inserto al final.
def insertarFinal(dato, cabeza):
    nuevo = crearNodo(dato)
    if cabeza is None:
        return nuevo
    actual= cabeza
    while actual["siguiente"] is not None:
        actual= actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza 

#Cuando la variable que usamos para recorrer la lista sea None, se rompe el while, mientras este verdadera, esta imprimiento el dato que seria el nombre.
#y señalizando el proximo nodo, cuando actual sea igual actual["siguiente"] se imprimira None, porque ya romperia el while 
def mostrar(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end= "→")
        actual= actual["siguiente"]
    print("None")

#Mientras que actual no sea None, recorrera nodo por nodo buscando que actual["dato"] sea igual al dato indicado y retornara su posicion, mientras no sea asi.
#recorrera los siguienes nodos e ira sumando 1 a posicion 
def buscar(cabeza, dato):
    actual = cabeza
    posicion= 0
    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual= actual["siguiente"]
        posicion += 1 
    return -1

#
def eliminar(dato, cabeza):
    if cabeza is None:
        return None, False
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True

    anterior= cabeza
    actual= cabeza["siguiente"]

    while actual is not None:
         if actual["dato"] == dato:
             anterior["siguiente"]= actual["siguiente"]
             return cabeza, True

         anterior= actual["siguiente"]
         actual= actual["siguiente"]
    return cabeza, False

def contar(cabeza):
    total= 0
    actual= cabeza
    while actual is not None:
        total += 1
        actual= actual["siguiente"]
    return total


def menu():
    cabeza = None

    while True:
        print("=== TURNOS DEL LABORATORIO ===")
        print("1. Agregar turno")
        print("2. Mostrar turnos")
        print("3. Buscar turno")
        print("4. Eliminar turno")
        print("5. Contar turnos")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre: ").strip()

                if not nombre:
                    print("El nombre no puede estar vacio.")
                else:
                    cabeza = insertarFinal(cabeza, nombre)
                    print("Turno agregado correctamente.")

            elif opcion == 2:
                mostrar(cabeza)

            elif opcion == 3:
                nombre = input("Ingrese el nombre a buscar: ").strip()

                if not nombre:
                    print("El nombre no puede estar vacio.")
                else:
                    posicion = buscar(cabeza, nombre)

                    if posicion == -1:
                        print("Estudiante no encontrado.")
                    else:
                        print(f"Estudiante encontrado en la posicion {posicion}")

            elif opcion == 4:
                nombre = input("Ingrese el nombre a eliminar: ").strip()

                if not nombre:
                    print("El nombre no puede estar vacio.")
                else:
                    cabeza, eliminado = eliminar(cabeza, nombre)

                    if eliminado:
                        print("Turno eliminado correctamente.")
                    else:
                        print("Estudiante no encontrado.")

            elif opcion == 5:
                print(f"Cantidad de turnos: {contar(cabeza)}")

            elif opcion == 0:
                print("Programa finalizado.")
                break

            else:
                print("Opcion invalida. Seleccione del 0 al 5.")

        except ValueError:
            print("Error: debe ingresar un numero.")


