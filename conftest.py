import pytest
from selenium import webdriver
import pytest_html
import pathlib
import base64

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": "reqres_2dbd7eae6cda425eb2aefbda8c8a5a50"}
    
#para capturar imagenes
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
#este metodo me devuelve un objeto que me permite identificar los distintos momentos 
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        
        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True)
#aca le decimos que saque la foto
        archivo = carpeta / f"{item.name}.png"
        
        driver.save_screenshot(str(archivo))
        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
        
        report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
        ]        