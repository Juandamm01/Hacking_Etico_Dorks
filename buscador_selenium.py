from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BusquedaWeb:
    
    def __init__(self):
        self.navegador = self.iniciar_navegador()

    def iniciar_navegador(self):
        navegadores = {
            "firefox": {
                "administrador": GeckoDriverManager,
                "servicio": FirefoxService,
                "opciones": webdriver.FirefoxOptions(),
                "driver": webdriver.Firefox
            },
            "chrome": {
                "administrador": ChromeDriverManager,
                "servicio": ChromeService,
                "opciones": webdriver.ChromeOptions(),
                "driver": webdriver.Chrome
            }
        }
        
        for nombre, datos in navegadores.items():
            try:
                return datos["driver"](
                    service=datos["servicio"](datos["administrador"]().install()),
                    options=datos["opciones"]
                )
            except:
                pass

        raise Exception("No se pudo iniciar ningún navegador.")

    def aceptar_cookies(self, id_boton):
        try:
            boton = WebDriverWait(self.navegador, 5).until(
                EC.element_to_be_clickable((By.ID, id_boton))
            )
            boton.click()
        except:
            pass  # No muestra nada si no hay cookies

    def esperar_si_captcha(self):
        try:
            self.navegador.find_element(By.CLASS_NAME, 'g-recaptcha')
            input("[!] reCAPTCHA detectado. Resuélvelo manualmente y presiona ENTER para continuar...")
        except:
            pass

    def buscar_en_google(self, texto_busqueda):
        self.navegador.get('https://www.google.com')
        self.aceptar_cookies(id_boton='L2AGLb')
        self.esperar_si_captcha()
        caja_busqueda = self.navegador.find_element(By.NAME, 'q')
        caja_busqueda.send_keys(texto_busqueda + Keys.ENTER)
        time.sleep(2)

    def obtener_resultados(self):

     resultados = self.navegador.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')
     lista_resultados = []

     for item in resultados:
        try:
            titulo = item.find_element(By.TAG_NAME, 'h3').text
            enlace = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            descripcion = item.find_element(By.CLASS_NAME, 'VwiC3b').text

            if titulo and enlace:
                lista_resultados.append({
                     "title": titulo,
                     "link": enlace,
                     "description": descripcion
                })
        except:
            continue

     return lista_resultados

    def cerrar(self):
        self.navegador.quit()
