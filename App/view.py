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
    print("3- (Requisito 2) Consultar video con mas dias en trending para un país especifico con recepción altamente positiva")
    print("4- (Requisito 3) Consultar video con mas dias en trending para una categoría especifica con recepción sumamente positiva")
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


def printCategoryList(catalog):
    """
    Imprime los nombres de las categorias cargadas
    """
    size = lt.size(catalog['category_names'])
    for i in range(1, size+1):
        element = lt.getElement(catalog['category_names'], i)
        print(element['name'])


def printReq1(lst):
    for video in lt.iterator(lst):
        print("trending_date: "+ str(video['trending_date'])+ ' title: '+ str(video['title']) + 
              ' channel_title: '+ str(video['channel_title'])+ ' publish_time: '+ str(video['publish_time'])
              + ' views: '+ str(video['views']) + ' likes: ' + str(video['likes'])+ ' dislikes: ' + str(video['dislikes']))


def printReq2(video, max):
    title = "title: " + str(video['title'])
    channel_title = " channel_title: " + str(video['channel_title'])
    country = " country: " + str(video['country'])
    ratio = int(video['likes'])/int(video['dislikes'])
    ratio_likes_dislikes = " ratio_likes_dislikes: " + str(ratio)
    dias = " Días: " + str(max)
    
    print(title + channel_title + country + ratio_likes_dislikes + dias)


def printReq4(lst):
    for video in lt.iterator(lst):
        title = "title: " + str(video['title'])
        channel_title = ' channel_title: ' + str(video['channel_title'])
        publish_time = ' publish_time: ' + str(video['publish_time'])
        views = ' views: ' + str(video['views'])
        likes = ' likes: ' + str(video['likes'])
        dislikes = ' dislikes: ' + str(video['dislikes'])
        comment_count = " comment_count: " + str(video['comment_count'])
        tag = " tags: " + str(video['tags'])

        print(title + channel_title + publish_time + views + likes + dislikes +comment_count + tag)


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
        printCategoryList(catalog)

    elif int(inputs[0]) == 2:

        number = input("Buscando los TOP ?: ")
        country = input("Buscando del Pais: ? ")
        category = input("Buscando en categoria: ? ")
  
        Req1 = controller.getReq1(catalog, category, country, int(number))
        printReq1(Req1)
        
    elif int(inputs[0]) == 3:
        country = input("Buscando del Pais: ? ")
        
        Req2 = controller.getReq2(catalog, country)
        printReq2(Req2[0], Req2[1])
        
    elif int(inputs[0]) == 4:
        category = input("Buscando en categoria: ? ")

    elif int(inputs[0]) == 5:
        number = int(input("Buscando los TOP ?: "))
        country = input("Buscando del Pais: ? ")
        tag = input("Buscando el tag: ?")

        Req4 = controller.getReq4(catalog, country, number, tag)

        printReq4(Req4)

    else:
        sys.exit(0)
sys.exit(0)
