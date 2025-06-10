import os
import re
import argparse

class BusquedaInteligente:
    """Permite buscar texto en archivos de un directorio usando expresiones regulares.

    Atributos:
        ruta_directorio (str): Ruta del directorio con los archivos.
        archivos (dict): Diccionario con nombre del archivo como clave y su contenido como valor.
    """

    def __init__(self, ruta_directorio):
        "Inicializa la clase BusquedaInteligente."
        self.ruta_directorio = ruta_directorio
        self.archivos = self._leer_archivos()

    def _leer_archivos(self):
        "Lee los archivos de texto del directorio y guarda su contenido."
        archivos = {}
        for nombre_archivo in os.listdir(self.ruta_directorio):
            ruta_archivo = os.path.join(self.ruta_directorio, nombre_archivo)
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    archivos[nombre_archivo] = archivo.read()
            except Exception as error:
                print(f"Error al leer el archivo {ruta_archivo}: {error}")
        return archivos

    def buscar_con_expresion(self, expresion_regular):
        "Busca coincidencias con una expresión regular en todos los archivos."
        resultados = {}
        for nombre_archivo, contenido in self.archivos.items():
            respuesta = ""
            while respuesta.lower() not in ("s", "n", "si", "no"):
                respuesta = input(f"El archivo '{nombre_archivo}' tiene {len(contenido)} caracteres. ¿Deseas buscar en él? (s/n): ")
            if respuesta.lower() in ("n", "no"):
                continue

            coincidencias = re.findall(expresion_regular, contenido, re.IGNORECASE)
            if coincidencias:
                resultados[nombre_archivo] = coincidencias
        return resultados


