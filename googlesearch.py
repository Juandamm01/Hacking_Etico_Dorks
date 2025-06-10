import requests
class Googlesearch:
    def __init__(self, api_key_google, buscador_id):
        self.api_key_google = api_key_google
        self.buscador_id = buscador_id


    def Search (self, query, start_page = 1, pages = 1, lang = "lang_es" ):
        resultados_finales = []
        resultados_por_paginas = 10
        for page in range(pages):
            start_index = (start_page - 1 ) * resultados_por_paginas + 1 + (page * resultados_por_paginas)
            url  = f"https://www.googleapis.com/customsearch/v1?key={self.api_key_google}&cx={self.buscador_id}&q={query}&start={start_index}&lr={lang}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                resultados = data.get("items")
                results = self.custom_results(resultados)
                resultados_finales.extend(results)
            else:
                print(f"Error al consultar la pagina: {page}: HTTP: {response.status_code}")
                break
        return resultados_finales

    
    def custom_results(self, resultados):
        custom_results = []
        for r in resultados:
            result = {}
            result["title"] = r.get("title")
            result["description"] = r.get("snippet")
            result["link"] = r.get("link")
            custom_results.append(result)
        return custom_results
        
