"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time as t
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sh
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(dat_est):

    catalog = {'videos': None, 'category_names': None}

    catalog['videos'] = lt.newList(dat_est)
    catalog['category_names'] = lt.newList(dat_est)

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)


def addCategory(catalog, cat):

    c = newCategory(cat['name'], cat['id'])

    lt.addLast(catalog['category_names'], c)

# Funciones para creacion de datos


def newCategory(name, id):

    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat

# Funciones de consulta


def getCategoryid(catalog,category_name):
    """
    Devuelve el id de una categoria del catalogo.
    Args:
        catalog: catalogo con la lista de videos y la lista de categorias
        category_name: nombre de la categoria que se consulta
    """
    for cat in lt.iterator(catalog['category_name']):
        if cat['name']==category_name:
            return cat['id']
    return None


def like_ratioCond(video, number):
    """
    Devuelve verdadero (True) si la taza de likes a dislikes es mayor a la condición representada por el 
    numero number
    Args:
        video: el video sobre el cual se esta evaluando la condición
        number: un numero float que representa el numero que debe superar la taza para que devuelva
        verdadero
    """
    cond = int(video['likes']/video['dislikes'])
    if cond > number:
        return True
    else:
        return False

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'likes'
        video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) > int(video2['likes']))


# Funciones de ordenamiento


def sortbyLikes(catalog, size, method): 
    sub_list = lt.subList(catalog['videos'], 1, size)

    sub_list = sub_list.copy()

    if method == "selectionsort":
        start_time = t.process_time()
        sorted = ss.sort(sub_list, cmpVideosByLikes)
        stop_time = t.process_time()
        delta = stop_time-start_time

    elif method == "insertionsort":
        start_time = t.process_time()
        sorted = ins.sort(sub_list, cmpVideosByLikes)
        stop_time = t.process_time()
        delta = stop_time-start_time

    elif method == "shellsort":
        start_time = t.process_time()
        sorted = sh.sort(sub_list, cmpVideosByLikes)
        stop_time = t.process_time()
        delta = stop_time-start_time

    return sorted, delta
