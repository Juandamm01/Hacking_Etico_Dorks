import os
import requests

class DescargarArchivos:
    """Clase para descargar archivos desde URLs y guardarlos localmente."""

    def __init__(self, directorio_destino):
        self.directorio = directorio_destino
        self._crear_directorio()

    def _crear_directorio(self):
        """Crea el directorio de destino si no existe."""
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)

    def descargar_archivo(self, url):
        try:
            nombre_archivo = url.split("/")[-1].split("?")[0]
            if not nombre_archivo:
                nombre_archivo = "archivo_descargado"
            ruta_completa = os.path.join(self.directorio, nombre_archivo)

            if os.path.exists(ruta_completa):
                print(f"Archivo: {nombre_archivo} ya existe, se omite la descarga\n")
                return

            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            with open(ruta_completa, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Archivo guardado como: {ruta_completa}\n")

        except Exception as e:
            print(f"Error al descargar el archivo {url}: {e}")

    def filtrar_descargar_archivos(self, urls, tipos_archivos=["all"]):
        if tipos_archivos == ["all"]:
            for url in urls:
                self.descargar_archivo(url)
        else:
            for url in urls:
                if any(url.endswith(f".{tipo}") for tipo in tipos_archivos):
                    self.descargar_archivo(url)
