# 🥷 Hacking Ético - Automatización de Dorks y Descargas Inteligentes

Este repositorio contiene un conjunto de scripts diseñados con fines **educativos** para automatizar tareas comunes en procesos de *reconocimiento pasivo* y análisis de información usando dorks de Google, búsquedas inteligentes en archivos locales, filtrado de resultados y descarga de documentos relevantes.

> **Proyecto desarrollado como parte del aprendizaje en Hacking Ético. Su uso debe ser responsable y legal.**

---

## Características Principales

- Búsquedas avanzadas con **Google Dorks** y Selenium
- Descarga automática de archivos de interés (.pdf, .docx, etc.)
- Análisis de contenido mediante **expresiones regulares**
- Filtro y presentación de resultados
- Automatización con Selenium y Google API
- Presentación de resultados en consola y HTML

---

## Estructura del Proyecto
├── buscador_selenium.py # Automatiza búsqueda con navegador usando Selenium
├── googlesearch.py # Utiliza Google Custom Search API
├── descargas_archivos.py # Descarga archivos de URLs filtradas
├── filtrado.py # Filtra resultados por tipo o palabra clave
├── resultados_parse.py # Extrae y organiza datos de los resultados
├── ninjadoorks.py # Ejecuta búsquedas con lista de dorks personalizada
├── plantilla.html # Plantilla HTML para mostrar resultados
├── dependencias.txt # Librerías necesarias
├── .env # Claves de API y configuración (no se sube)
├── Descargas/ # Carpeta donde se almacenan los archivos descargados
├── pycache/ # Archivos cacheados automáticamente por Python
└── README.md # Este Archivo que contiene la breve explicación del funcionamiento del Proyecto

## Requisitos del Entorno

> **Se recomienda el uso de Miniconda para aislar el entorno de desarrollo.**

### Crear entorno virtual con Miniconda

```bash
conda create -n hacking_dorks python=3.11
conda activate hacking_dorks



### Las dependencias que se usaran""
pip install requests python-dotenv rich selenium webdriver_manager

| Librería            | Propósito                                              |
| ------------------- | ------------------------------------------------------ |
| `requests`          | Peticiones HTTP                                        |
| `python-dotenv`     | Cargar variables de entorno desde archivo `.env`       |
| `rich`              | Imprimir resultados coloridos y organizados en consola |
| `selenium`          | Automatizar navegador para búsquedas                   |
| `webdriver_manager` | Instalar y administrar drivers automáticamente         |

### Las Variables De Entorno
Crea un archivo .env con tus claves de la API de Google:

GOOGLE_API_KEY=tu_clave_api
GOOGLE_CX_ID=tu_id_buscador_personalizado

 Flujo de Trabajo Recomendado
 Crear y cargar dorks personalizados en ninjadoorks.py

 Ejecutar búsquedas con googlesearch.py o buscador_selenium.py

 Usar filtrado.py para refinar resultados

Descargar archivos interesantes con descargas_archivos.py

Analizar datos o visualizar resultados con HTML o consola (Rich)

Autor
Juan David (@Juandamm01)
