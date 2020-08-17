"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

"""
Esto es un comentario de prueba. No olvidar borrar
Esto es un comentario de prueba. No olvidar borrar
Esto es un comentario de prueba. No olvidar borrar
Esto es un comentario de prueba. No olvidar borrar
"""

import config as cf
import sys
import csv
from time import process_time 

"""
def loadCSVFile (file, lst, sep=";"):
   
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
            
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

"""

def loadCSVFile (file,file2, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """

    lst = []
    del lst[:]
    print("Cargando archivo ....")
    try:
        with open(file, encoding="utf-8") as csvfile:
            csvfile2=open(file2, encoding="utf-8")
            linea=csvfile.readline()
            linea=csvfile.readline()
            linea2=csvfile2.readline()
            linea2=csvfile2.readline()
            while(len(linea)>0):               
                diccio={}             
                datos=linea.split(";")
                datos2=linea2.split(";")
                diccio["id"]=datos[0]
                diccio["budget"]=datos[1]
                diccio["genres"]=datos[2]
                diccio["imdb_id"]=datos[3]
                diccio["original_language"]=datos[4]
                diccio["original_title"]=datos[5]
                diccio["overview"]=datos[6]
                diccio["popularity"]=datos[7]
                diccio["production_companies"]=datos[8]
                diccio["production_countries"]=datos[9]
                diccio["release_date"]=datos[10]
                diccio["revenue"]=datos[11]
                diccio["runtime"]=datos[12]
                diccio["spoken_languages"]=datos[13]
                diccio["status"]=datos[14]
                diccio["tagline"]=datos[15]
                diccio["title"]=datos[16]
                diccio["vote_average"]=datos[17]
                diccio["vote_count"]=datos[18]
                diccio["production_companies_number"]=datos[19]
                diccio["production_countries_number"]=datos[20]
                diccio["spoken_languages_number"]=datos[21].replace("\n","")
                diccio["actor1_name"]=datos2[1]
                diccio["actor1_gender"]=datos2[2]
                diccio["actor2_name"]=datos2[3]
                diccio["actor2_gender"]=datos2[4]
                diccio["actor3_name"]=datos2[5]
                diccio["actor3_gender"]=datos2[6]
                diccio["actor4_name"]=datos2[7]
                diccio["actor4_gender"]=datos2[8]
                diccio["actor5_name"]=datos2[9]
                diccio["actor5_gender"]=datos2[10]
                diccio["actor_number"]=datos2[11]
                diccio["director_name"]=datos2[12]
                diccio["director_number"]=datos2[13]
                diccio["producer_name"]=datos2[14]
                diccio["producer_number"]=datos2[15]
                diccio["screenplay_name"]=datos2[16]
                diccio["editor_name"]=datos2[17].replace("\n","")
                lst.append(diccio)                
                linea=csvfile.readline()
                linea2=csvfile2.readline()

             
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):

    print (lst[0])
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    contador=0
    sumatoria=0
    for i in range (0,len(lst)-2) :
        if lst[i]["director_name"]==criteria and float(lst[i]["vote_average"]) >= 6:
            #print(lst2[i]["director_name"]) 
            #print((lst[i]["vote_average"]))
            contador+=1
            sumatoria+=float(lst[i]["vote_average"])

    promedio = 0
    if contador > 0:
        promedio = sumatoria/contador
    
    return contador, promedio


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listac = [] #instanciar una lista vacia
    listar =[]
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile ("SmallMoviesDetailsCleaned.csv","SmallMoviesDetailsCleaned.csv", lst, sep=";")
                #loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", listac) #llamar funcion cargar datos
                #loadCSVFile("Data/MoviesCastingRaw-small.csv",listar )
                print("Datos cargados, "+str(len(lst))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(listac)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(listac))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                columna_busqueda = input ("Ingrese el nombre de la columna que desea buscar: ")
                criterio = input('Ingrese el criterio de búsqueda para realizar el conteo de coincidencias: ')
                counter=countElementsFilteredByColumn(criterio, columna_busqueda, lst) #filtrar una columna por criterio  
                print( "\nPara la busqueda de {} en la columna {}, se tienen {} coincidencias" .format(criterio, columna_busqueda, counter) )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter,promedio=countElementsByCriteria(criteria,listac,listar)
                print("En total, hay ",counter," películas del director: '", criteria ,".' Dichas películas tuvieron una votacion promedio de: " , promedio)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()



