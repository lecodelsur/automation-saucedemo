from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

from utils.reader import read_productos_json

def test_cart(driver):
    try:
        logger.info("Iniciando la prueba del carrito")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")
    #guardo en prodcuto el primer item que aparece en el diccionario del json    
        logger.info("Leyendo el primer producto del archivo JSON")
        producto = read_productos_json()[0]
        logger.info(f"Producto leído: {producto}")
    #Aca le digo que agregue la clave del primer producto que quiero del json
        inventory_page.agregar_producto(producto["nombre"])
    #ACa hago mi prmiera validacion
        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Producto agregado al carrito correctamente")
    #ir al carrito 
        inventory_page.ir_al_carrito()
        logger.info("Navegando al carrito")
    #validar nombre y precio contra el json
        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Nombre del producto en el carrito es correcto")
        assert cart_page.obtner_precio_producto() == producto["precio"]
        logger.info("Precio del producto en el carrito es correcto")    
    except Exception:
        logger.exception("Error en la prueba del carrito", exc_info=True)
        raise