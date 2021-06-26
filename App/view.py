"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (Requisito 1) Consultar los Top x videos por likes de un pais, de una categoria especifica")
    print("3- (Requisito 2) Consultar video con mas dias en trending para un pais especifico con recepción altamente positiva")
    print("4- (Requisito 3) Consultar video con mas dias en trending para una categoria especifica con recepción sumamente positiva")
    print("5- (Requisito 4) Consultar los Top x videos con mas comentarios en un pais con un tag especifico")
    print("0- Salir")


def printInfoMenu1():
    print("\t 1- Array (ARRAY_LIST)")
    print("\t 2- Lista encadenada(LINKED_LIST)")


def printInfoMenu2():
    print("Tipos de algoritmos de ordenamiento ")
    print("\t 1- Selection")
    print("\t 2- Insertion")
    print("\t 3- Shell")
    print("\t 4- Quick")
    print("\t 5- Merge")


def initCatalog(dat_est):
    """
    Inicializa el catologo de libros
    """
    return controller.initCatalog(dat_est)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def firstInfo(first):
    print('Titulo: ' + str(first['title']))
    print('Titulo del canal: ' + str(first['channel_title']))
    print('Fecha de tendencia: ' + str(first['trending_date']))
    print('Pais: ' + str(first['country']))
    print('Vistas: ' + str(first['views']))
    print('Likes: ' + str(first['likes']))
    print('Dislikes: ' + str(first['dislikes']))


def printCategoryList(catalog):
    """
    Imprime los nombres de las categorias cargadas
    """
    size = lt.size(catalog['category_names'])
    for i in range(1, size+1):
        element = lt.getElement(catalog['category_names'], i)
        print(element['name'])


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printInfoMenu1()
        inputs1 = input('Seleccione el tipo de estructura de datos que quiere implementar\n')
        if int(inputs[0]) == 1:
            dat_est = "ARRAY_LIST"
        if int(inputs1[0]) == 2:
            dat_est = "LINKED_LIST"

        print("Cargando información de los archivos ....")

        catalog = initCatalog(dat_est)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        first = lt.firstElement(catalog['videos'])
        print('Primer video cargado: ')
        firstInfo(first)

        print('Lista de categorias: ')
        printCategoryList(catalog)

    elif int(inputs[0]) == 2:
        printInfoMenu2()
        sort = input("Seleccione un método de ordenamiento para el algoritmo: ")

        if int(sort[0]) == 1:
            method = "selectionsort"
        elif int(sort[0]) == 2:
            method = "insertionsort"
        elif int(sort[0]) == 3:
            method = "shellsort"
        elif int(sort[0]) == 4:
            method = "quicksort"
        elif int(sort[0]) == 5:
            method = "mergesort"

        size = lt.size(catalog['videos'])

        menor = False

        while menor is False:

            q_size = input("Eliga la muestra de la sublista: ")

            if int(q_size) <= size:
                size = int(q_size)
                menor = True
            else:
                print("Eliga un valor que no exceda el tamaño de la lista")

        number = input("Buscando los TOP ?: ")
        country = input("Buscando del Pais: ? ")
        category = input("Buscando en categoria: ? ")

        sorted = controller.sortbyLikes(catalog, size, method)

        for e in range(1, size):

            ele = lt.getElement(sorted[0], e)

            print(ele['title'], ele['likes'])
        print("El tiempo de procesamiento es de: " + str(round(sorted[1], 2)) + " ms")
    elif int(inputs[0]) == 3:
        country = input("Buscando del Pais: ? ")

    elif int(inputs[0]) == 4:
        category = input("Buscando en categoria: ? ")

    elif int(inputs[0]) == 5:
        number = input("Buscando los TOP ?: ")
        country = input("Buscando del Pais: ? ")
        tags = input("Buscando el tag: ?")

    else:
        sys.exit(0)
sys.exit(0)
