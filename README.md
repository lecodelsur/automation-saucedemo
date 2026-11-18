
# 🧪 Automatización QA - Saucedemo

Proyecto de automatización de pruebas End-to-End (E2E) y pruebas de API desarrollado con **Python** para el curso de **Talento Tech**. El framework está estructurado bajo el patrón de diseño **Page Object Model (POM)**, integrando generación de reportes visuales, captura de evidencias y ejecución automatizada mediante **GitHub Actions**.

---

## 🛠️ Tecnologías y Herramientas

* **Python 3.x** – Lenguaje principal de desarrollo.
* **Selenium WebDriver** – Automatización de interacciones en el navegador web.
* **Pytest** – Framework de ejecución y gestión de pruebas.
* **Pytest-HTML** – Generación de reportes detallados en formato HTML.
* **Pytest-Check** – Validaciones múltiples (*soft assertions*) dentro de un mismo test.
* **Requests** – Automatización y validación de pruebas de API REST.
* **Git & GitHub Actions** – Control de versiones e Integración Continua (CI).

---

## 📁 Estructura del Proyecto

```text
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

Para ejecutar únicamente las pruebas de API:
```bash
pytest tests/test_api.py -s
```

### 📊 Reportes y Evidencias
Al finalizar la ejecución, se genera automáticamente un reporte visual en la carpeta `reports/` junto con las capturas de pantalla correspondientes en `reports/screenshots/`.

---

## 🧪 Casos de Prueba Implementados

* **Autenticaci贸n (`test_login.py`):** Validación de inicio de sesión exitoso y manejo de credenciales.
* **Inventario (`test_inventory.py`):** Exploración y selección de productos en el catálogo.
* **Carrito de Compras (`test_cart.py`):** Agregado y verificación de artículos dentro del carrito.
* **Pruebas de API (`test_api.py`):** Validación de c贸digos de estado HTTP, cabeceras, estructura JSON, datos de respuesta y tiempos de ejecución.

---

## 👤 Autor

Desarrollado por **Sergio E. Sánchez Castillo** para el curso de **Talento Tech**.