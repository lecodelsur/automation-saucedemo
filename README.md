# 🧪 Automatización QA - Saucedemo

Proyecto de automatización de pruebas End-to-End (E2E) y pruebas de API desarrollado con **Python** para el curso de **Talento Tech**. El framework está estructurado bajo el patrón de diseño **Page Object Model (POM)**, integrando generación de reportes visuales, captura de evidencias y ejecución automatizada mediante **GitHub Actions**[cite: 1, 2, 3].

---

## 🛠️ Tecnologías y Herramientas

* **Python 3.x** – Lenguaje principal de desarrollo.
* **Selenium WebDriver** – Automatización de interacciones en el navegador web.
* **Pytest** – Framework de ejecución y gestión de pruebas[cite: 1, 3].
* **Pytest-HTML** – Generación de reportes detallados en formato HTML[cite: 1, 3].
* **Pytest-Check** – Validaciones múltiples (*soft assertions*) dentro de un mismo test.
* **Requests** – Automatización y validación de pruebas de API REST.
* **Git & GitHub Actions** – Control de versiones e Integración Continua (CI)[cite: 2, 3].

---

## 📁 Estructura del Proyecto

```text
├── .github/workflows/   # Configuración de CI/CD en GitHub Actions (tests.yml)
├── data/                # Archivos de datos de prueba (CSV y JSON)[cite: 1, 3]
├── features/            # Escenarios y definiciones de pruebas[cite: 3]
├── logs/                # Registros de ejecución del framework[cite: 1, 3]
├── pages/               # Clases con el patrón Page Object Model (POM)[cite: 1, 3]
├── reports/             # Reportes HTML generados y carpeta de screenshots[cite: 1, 3]
├── tests/               # Scripts de pruebas automatizadas (UI y API)[cite: 1, 3]
├── utils/               # Utilidades auxiliares (logger, lectores de archivos)[cite: 1, 3]
├── conftest.py          # Fixtures y configuraciones globales de Pytest[cite: 1, 3]
├── pytest.ini           # Configuración de ejecución de Pytest[cite: 1, 3]
└── requirements.txt     # Dependencias del proyecto[cite: 3]

## Instalación y configuracion

Bash

git clone [https://github.com/lecodelsur/automation-saucedemo.git](https://github.com/lecodelsur/automation-saucedemo.git)
cd automation-saucedemo

## Crea y activa un entorno virtual

Bash

# En Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate

# En macOS / Linux
python3 -m venv venv
source venv/bin/activate

## instala las dependencias del proyecto:

Bash

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

##Ejecución de las pruebas

Bash

pytest -s

##Ejecución de pruebas específicas de API

Bash

pytest tests/test_api.py -s

## Casos de prueba

Autenticación (test_login.py): Validación de inicio de sesión exitoso y manejo de credenciales. 
Inventario (test_inventory.py): Exploración y selección de productos en el catálogo. 
Carrito de Compras (test_cart.py): Agregado y verificación de artículos dentro del carrito.
Pruebas de API (test_api.py): Validación de códigos de estado HTTP, cabeceras, estructura JSON, datos de respuesta y tiempos de ejecución.

## Autor

Desarrollado por Sergio E. Sánchez Castillo para el curso de Talento Tech