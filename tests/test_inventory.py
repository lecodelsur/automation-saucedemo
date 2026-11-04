from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Iniciando la prueba de inventario")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        logger.info("ingresando a la pagina web")
        driver.get("https://www.saucedemo.com/")
        logger.info("ingresando credenciales para iniciar sesion")
    #Me logueo›
        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")
    #ME fijo si hay productos en mi página
        productos = inventory_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")
    #Me fijo si la cantidad de productos es mayor que cero
        assert len(productos) > 0
        logger.info("Cantidad de productos mayor a cero")
    #Me fijo que el nombre del primer producto sea el texto que me retornó obtener_nombre_primer_producto
        assert inventory_page.obtener_nombre_primer_producto () == "Sauce Labs Backpack"
        logger.info("Nombre del primer producto es correcto")
    #Me fijo que el precio del primer producto sea el texto que me retornó obtener_precio_primer_producto
        assert inventory_page.obtener_precio_primer_producto () == "$29.99"
        logger.info("Precio del primer producto es correcto")
    #Validar menu y filtro vicible (que devuelven verdadero o falso)
        assert inventory_page.menu_visible()
        logger.info("Menu visible")
        assert inventory_page.filtro_visible()
        logger.info("Filtro visible")
    except Exception:
        logger.exception("Error en la prueba de inventario", exc_info=True)
        raise