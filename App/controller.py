﻿"""
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
 """

import config as cf
import model
import csv
assert cf

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog():

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos


def loadData(catalog):

    loadVideos(catalog)
    loadCategory(catalog)


def loadVideos(catalog):

    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategory(catalog):

    catfile = cf.data_dir + 'Videos/category-id.csv'
    file = open(catfile, encoding='utf-8')
    input_file = csv.DictReader(file, delimiter='\t')

    for categoria in input_file:
        model.addCategory(catalog, categoria)

# Funciones de ordenamiento


def sortbyLikes(catalog, size, method):

    return model.sortbyLikes(catalog, size, method)

# Funciones de consulta sobre el catálogo


def getReq1(catalog, category_name, country, number):
    
    return model.getReq1(catalog, category_name, country, number)


def getReq3(catalog, category_name): 

    return model.getReq3(catalog, category_name)

 
def getReq4(catalog, country, number, tag): 

    return model.getReq4(catalog, country, number, tag )

