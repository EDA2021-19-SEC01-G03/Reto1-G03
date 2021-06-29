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
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():

    catalog = {'videos': None, 'category_names': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['category_names'] = lt.newList('ARRAY_LIST')

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


def getCategoryid(catalog, category_name):
    """
    Devuelve el id de una categoria del catalogo.
    Args:
        catalog: catalogo con la lista de videos y la lista de categorias
        category_name: nombre de la categoria que se consulta
    """
    for cat in lt.iterator(catalog['category_names']):
        if category_name in cat['name']:
            return cat['id']
    return "error"


def like_ratioCond(video, number):
    """
    Devuelve verdadero (True) si la taza de likes a dislikes es mayor a la condición representada por el
    numero number
    Args:
        video: el video sobre el cual se esta evaluando la condición
        number: un numero float que representa el numero que debe superar la tasa para que devuelva
        verdadero
    """
    
    if int(video['dislikes']) != 0:
        cond = int(video['likes'])/int(video['dislikes'])
        if cond > number:
            return True
        else:
            return False
    elif int(video['dislikes']) == 0: 
        return True



def getReq1(catalog, category_name, country, number):
    """
    """
    sub_list = lt.newList("ARRAY_LIST")
    category_id = getCategoryid(catalog, category_name)
    for video in lt.iterator(catalog['videos']):
        
        if video['category_id'] == category_id and video['country'] == country:
            lt.addLast(sub_list, video)
    sorted_list = sortbyLikes(sub_list)
    top_n = lt.subList(sorted_list, 1, number)

    return top_n


def getReq3(catalog, category_name):

    result = lt.newList("ARRAYLIST")
    cat_id = getCategoryid(catalog, category_name)

    for video in lt.iterator(catalog['videos']):

        ratio = like_ratioCond(video, 20)

        if cat_id == video['category_id'] and ratio:
            lt.addLast(result, video)

    result_sorted = sortbyTrendingDate(result)

    x = 1
    list_days = lt.newList("ARRAY_LIST")

    while x < lt.size(result_sorted):

        vid_x = lt.getElement(result_sorted, x)
        name_x = vid_x['title']
        contador = 0
        j = x
        dates = []

        while j < lt.size(result_sorted):
            vid_j = lt.getElement(result_sorted, j)

            if vid_j['title'] == name_x and (vid_j['trending_date'] not in dates):
                contador += 1
                dates.append(vid_j['trending_date'])

            j += 1

        vid_x['days'] = contador

        lt.addLast(list_days, vid_x)

        x += 1

    resultado = sortbyDays(list_days)

    return resultado


def getReq4(catalog, country, number, tag):

    result = lt.newList("ARRAY_LIST")

    for video in lt.iterator(catalog['videos']):

        if (tag in video['tags']) and (country == video['country']):

            lt.addLast(result, video)

    sorted = sortbyComm(result)

    first_n = lt.subList(sorted, 1, number)

    return first_n


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'likes'
        video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) > int(video2['likes']))


def cmpVideosByComm(video1, video2):

    return (int(video1['comment_count']) > int(video2['comment_count']))


def cmpVideosbyName(video1, video2): 

    return (video1['title'] > video2['title'])


def cmpVideosbyDays(video1, video2): 

    return (video1['days'] > video2['days'])


# Funciones de ordenamiento


def sortbyComm(lst):

    sub_list = lst.copy()
    sorted = ms.sort(sub_list, cmpVideosByComm)
    return sorted

def sortbyLikes(lst):
    sub_list = lst.copy()
    sorted = ms.sort(sub_list, cmpVideosByLikes)
  
    return sorted


def sortbyName(lst):
    sub_list = lst.copy()
    sorted = ms.sort(sub_list, cmpVideosbyName)
    
    return sorted


def sortbyDays(lst): 
    sub_list = lst.copy()
    sorted = ms.sort(sub_list, cmpVideosbyDays)

    return sorted