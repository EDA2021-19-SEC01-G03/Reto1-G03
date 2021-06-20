﻿"""
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


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (Requisito 1) Consultar los Top x videos por likes de un pais, de una categoria especifica")
    print("3- (Requisito 2) Consultar video con mas dias en trending para un pais especifico con recepción altamente positiva")
    print("4- (Requisito 3) Consultar video con mas dias en trending para una categoria especifica con recepción sumamente positiva")
    print("5- (Requisito 4) Consultar los Top x videos con mas comentarios en un pais con un tag especifico")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catologo de libros
    """
    return controller.initCatalog()


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


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        first = lt.firstElement(catalog['videos'])
        print('Primer video cargado: ')
        firstInfo(first)

        print('Lista de categorias: ')
        print(catalog['category_names'])

    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        country = input("Buscando del Pais: ? ")
        category = input("Buscando en categoria: ? ")

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
