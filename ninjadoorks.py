from dotenv import load_dotenv, set_key
import os
import argparse
import sys
from googlesearch import Googlesearch
from resultados_parse import ResultadosParse
from descargas_archivos import DescargarArchivos
from filtrado import BusquedaInteligente
from buscador_selenium import BusquedaWeb

load_dotenv()

def env_config():
    api_key_google = input("Introduce tu API KEY de Google: ")
    buscador_id = input("Introduce el ID del buscador personalizado de Google: ")
    set_key(".env", "api_key_google", api_key_google)
    set_key(".env", "buscador_id", buscador_id)

def load_env(configure_env):
    env_exists = os.path.exists(".env")

    if not env_exists or configure_env:
        env_config()
        print("Archivo .env configurado satisfactoriamente.")
        sys.exit(0)

    load_dotenv()

    api_key_google = os.getenv("api_key_google")
    buscador_id = os.getenv("buscador_id")

    return (api_key_google, buscador_id)

def main(query, configure_env, start_page, pages, lang, salida_json, salida_html, descarga, directorio, expresion, selenium):
    
    if not query:
        print("Debes indicar una consulta con el comando -q.")
        print("Usa -h para obtener ayuda.")
        sys.exit(1)

    elif selenium:
        Buscador = BusquedaWeb()
        Buscador.buscar_en_google(query)
        Buscador.esperar_si_captcha()
        resultados = Buscador.obtener_resultados()
        Buscador.cerrar()
    
    else:
         api_key_google, buscador_id = load_env(configure_env=configure_env)
         gSearch = Googlesearch(api_key_google, buscador_id)
         resultados = gSearch.Search(query, pages=pages, start_page=start_page, lang=lang)

    resultados_parse = ResultadosParse(resultados)
    resultados_parse.mostrar_pantalla()

    if salida_json:
        resultados_parse.exportar_json(salida_json)

    if salida_html:
        resultados_parse.exportar_html(salida_html)

    if descarga:
        tipos_de_archivos = descarga.split(",")
        urls = [resultado['link'] for resultado in resultados]
        FDescargas = DescargarArchivos("Descargas")
        FDescargas.filtrar_descargar_archivos(urls, tipos_de_archivos)

    if expresion:
        if not directorio:
            print("Debes especificar un directorio usando -d o --directorio para realizar búsquedas con expresiones regulares.")
            sys.exit(1)

        buscador = BusquedaInteligente(directorio)
        resultados_regex = buscador.buscar_con_expresion(expresion)

        print("\nResultados encontrados con la expresión regular:\n")
        for archivo, coincidencias in resultados_regex.items():
            print(f"{archivo}:")
            for coincidencia in coincidencias:
                print(f"\t- {coincidencia}")

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Herramienta para automatizar búsquedas con dorks en Google.")
    parse.add_argument("-q", "--query", type=str, help="Especifica el dork que deseas buscar (ej: site:.edu inurl:login).")
    parse.add_argument("-c", "--configure", action='store_true', help="Inicializa el proceso de configuración del archivo .env.")
    parse.add_argument("-start-page", type=int, default=1, help="Página de inicio para obtener los resultados de búsqueda.")
    parse.add_argument("--pages", type=int, default=1, help="Número de páginas de resultados de búsqueda.")
    parse.add_argument("--lang", type=str, default="lang_es", help="Idioma de los resultados (por defecto 'lang_es').")
    parse.add_argument("--json", type=str, help="Ruta de salida para exportar los resultados en formato JSON.")
    parse.add_argument("--html", type=str, help="Ruta de salida para exportar los resultados en formato HTML.")
    parse.add_argument("--download", type=str, default=None, help="Tipos de archivos a descargar (ej: pdf,docx,xls).")
    parse.add_argument("-d", "--directorio", type=str, help="Ruta del directorio para aplicar expresiones regulares.")
    parse.add_argument("-e", "--expresion", type=str, help="Expresión regular a buscar dentro de los archivos.")
    parse.add_argument("--selenium", action="store_true", help="Genera búsquedas automatizadas con Selenium")
    args = parse.parse_args()

    main(args.query, args.configure, args.start_page, args.pages, args.lang,
         args.json, args.html, args.download, args.directorio, args.expresion,
         args.selenium)
