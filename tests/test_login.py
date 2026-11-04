import pytest
from pages.login_page import LoginPage
from utils.reader import read_users_csv
from utils.logger import logger


# Asegurate de que figure exactamente así, con una coma separando los textos fijos
#aca le digo que trabaje con data al lector de CSV
@pytest.mark.parametrize(
    "data",read_users_csv())

def test_login(driver,data):
    try:    
        logger.info(f"Ejecutando test_login con usuario: {data['usuario']} y tipo de usuario: {data['tipo_usuario']}")
    # Se abre el navegador
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Navegador abierto y página de login cargada")

    # accion de alto nivel
        login_page.login(data["usuario"],data["password"])
        logger.info(f"Intentando login con usuario: {data['usuario']} y password: {data['password']}")
    #aca valido la tercer columna de users.csv
        if data["tipo_usuario"] == "user_ok":

            assert "/inventory.html" in driver.current_url
            logger.info(f"Login exitoso para usuario: {data['usuario']}")
        elif data["tipo_usuario"] == "user_error":
    #creo una variable para guardar el error y me fijo que en error se encuentre "Epic sadface"
            error = login_page.obtener_mensaje_error()
            print (error)
            logger.info(f"Mensaje de error obtenido para usuario: {data['usuario']}")
            assert "Epic sadface" in error
    except Exception:
        logger.exception(f"Error en test_login con usuario: {data['usuario']}")
        raise
            
