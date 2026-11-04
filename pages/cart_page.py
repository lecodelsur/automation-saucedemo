from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
#Se programan las acciones y selectores inherentes a esa pagina en particular.
class CartPage:
    def __init__(self,driver):
        self.driver = driver
#inicializo la variable de la espera implícita con 10 segundos        
        self.wait = WebDriverWait(driver,10)

    def obtener_nombre_producto(self):
#al buscar un valor usamos return y le aplicamos una espera por que es dinámico y puede tardar y lo tomamos como texto  
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_name"))).text
    
    def obtner_precio_producto(self):
        precio = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_price"))).text
#convierto a decimal pero el simbolo $ lo reemplazo por vacio        
        return float(precio.replace("$",""))
    