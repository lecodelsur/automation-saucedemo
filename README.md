# 🧪 Automatizaci贸n QA - Saucedemo

Proyecto de automatizaci贸n de pruebas End-to-End (E2E) y pruebas de API desarrollado con **Python** para el curso de **Talento Tech**. El framework est谩 estructurado bajo el patr贸n de dise帽o **Page Object Model (POM)**, integrando generaci贸n de reportes visuales, captura de evidencias y ejecuci贸n automatizada mediante **GitHub Actions**.

---

## 🛠️ Tecnologías y Herramientas

* **Python 3.x** 鈥?Lenguaje principal de desarrollo.
* **Selenium WebDriver** 鈥?Automatizaci贸n de interacciones en el navegador web.
* **Pytest** 鈥?Framework de ejecuci贸n y gesti贸n de pruebas.
* **Pytest-HTML** 鈥?Generaci贸n de reportes detallados en formato HTML.
* **Pytest-Check** 鈥?Validaciones m煤ltiples (*soft assertions*) dentro de un mismo test.
* **Requests** 鈥?Automatizaci贸n y validaci贸n de pruebas de API REST.
* **Git & GitHub Actions** 鈥?Control de versiones e Integraci贸n Continua (CI).

---

## 📁 Estructura del Proyecto

├── .github/workflows/   # Configuración de CI/CD en GitHub Actions (tests.yml)
├── data/                # Archivos de datos de prueba (CSV y JSON)
├── features/            # Escenarios y definiciones de pruebas
├── logs/                # Registros de ejecución del framework
├── pages/               # Clases con el patrón Page Object Model (POM)
├── reports/             # Reportes HTML generados y carpeta de screenshots
├── tests/               # Scripts de pruebas automatizadas (UI y API)
├── utils/               # Utilidades auxiliares (logger, lectores de archivos)
├── conftest.py          # Fixtures y configuraciones globales de Pytest
├── pytest.ini           # Configuración de ejecución de Pytest
└── requirements.txt     # Dependencias del proyecto





## ⚙️ Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/lecodelsur/automation-saucedemo.git
   cd automation-saucedemo
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   # En Windows (PowerShell)
   python -m venv venv
   venv\Scripts\Activate

   # En macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias del proyecto:**
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

---

## 🏃‍♂️ Ejecución de las Pruebas

Para ejecutar toda la suite de pruebas mostrando las salidas en consola:
```bash
pytest -s
```

Para ejecutar 煤nicamente las pruebas de API:
```bash
pytest tests/test_api.py -s
```

### 📊 Reportes y Evidencias
Al finalizar la ejecuci贸n, se genera autom谩ticamente un reporte visual en la carpeta `reports/` junto con las capturas de pantalla correspondientes en `reports/screenshots/`.

---

## 🧪 Casos de Prueba Implementados

* **Autenticaci贸n (`test_login.py`):** Validaci贸n de inicio de sesi贸n exitoso y manejo de credenciales.
* **Inventario (`test_inventory.py`):** Exploraci贸n y selecci贸n de productos en el cat谩logo.
* **Carrito de Compras (`test_cart.py`):** Agregado y verificaci贸n de art铆culos dentro del carrito.
* **Pruebas de API (`test_api.py`):** Validaci贸n de c贸digos de estado HTTP, cabeceras, estructura JSON, datos de respuesta y tiempos de ejecuci贸n.

---

## 👤 Autor

Desarrollado por **Sergio E. S谩nchez Castillo** para el curso de **Talento Tech**.