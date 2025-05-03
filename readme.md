from docx import Document

# Crear el documento
doc = Document()
doc.add_heading('README', 0)

# Contenido del README
readme_content = """
🧪 Testing Automation: 🐍 Selenium 4.5 + Behave

SELENIUM-PYTHON

Selenium + Pytest + Behave (Gherkin) en VSCode
Explora la documentación »
Ver Demo

🌟 Sobre este Proyecto

Hola, soy Emanuel Restrepo, un apasionado del testing y la automatización de pruebas con Selenium y Python.
Este proyecto combina Selenium, Pytest y Behave (Gherkin) bajo el patrón Page Object Model (POM) para automatizar interacciones con aplicaciones web, siguiendo buenas prácticas de la industria.

Objetivos del proyecto:
- Mostrar habilidades avanzadas en QA Automation.
- Construir un framework reutilizable, limpio y escalable.
- Enseñar a otros testers cómo estructurar un proyecto profesional.
- Usar integración de BDD (Gherkin) y pruebas E2E automatizadas.

🚀 Cómo Empezar

1️⃣ Pre-requisitos
✅ Tener instalado Anaconda.
✅ Confirmar su instalación:
conda --version
✅ Configurar la variable de entorno:
C:\\Users\\Username\\anaconda3

2️⃣ Clonar el Proyecto
git clone https://github.com/Emanuelrestrepo22/selenium-py-POM.git

3️⃣ Configurar el Entorno
1. Abre VS Code.
2. Usa Ctrl+Shift+P → Python: Create Environment.
3. Selecciona Conda y la versión recomendada.
4. Espera a que se cree el entorno .conda.
5. Activa el entorno:
conda activate <full_path_env>

4️⃣ Instalar Dependencias
pip install -r requirements.txt

5️⃣ Configurar Variables de Entorno
El proyecto requiere un archivo .env (no incluido por seguridad) ubicado en la carpeta raíz.
Debes crearlo manualmente con las variables necesarias, por ejemplo:
BASE_URL=https://www.saucedemo.com
USER_NAME=standard_user
PASSWORD=secret_sauce

6️⃣ Ejecutar Pruebas
✅ Para pruebas con Pytest:
pytest -v --html=report.html --self-contained-html

✅ Para escenarios BDD (Behave):
behave features/

✅ Desde VS Code:
Usa el panel de Testing (ícono ⚡) para ver, correr y debuggear tus tests.

🏗️ Estrategia de Pruebas y Diseño
- Patrón aplicado: Page Object Model (POM).
- Frameworks: Selenium 4, Pytest, Behave.
- Prácticas:
  - Nomenclatura clara para test files:
    test_{GXID}_{StoryShortName}.py
    Ejemplo:
    test_GX50_AgregarItemsAlCart.py
  - Ubicación correcta de tests en tests/coverage/.
  - Evitar usar fixtures como POM.
  - Aplicación ordenada de comandos repetitivos.
  - Integración con pipelines CI (sanity.yml, regression.yml).

🗂️ Estructura del Proyecto
/pages            # Page Object Models
/tests           # Suites de prueba E2E
/features        # Archivos Gherkin (.feature) para Behave
/conftest.py     # Configuración global de tests
/.env            # Variables de entorno (no incluido, crear manualmente)
/requirements.txt # Dependencias del proyecto

🧪 Ejemplo de Expectativas (Assertions)
✔ Login exitoso → mensaje “Welcome!”.
✔ Agregar al carrito → precio total correcto.
✔ Completar checkout → mensaje “Order Confirmed!”.
✔ Campos inválidos → error mostrado.

🔧 Versiones y Dependencias
✅ Ver la versión de Selenium:
python -c "import selenium; print(selenium.__version__)"

🛠️ Pasos Serie para Ejecutar el Proyecto
Paso 1: Clonar el Repositorio
git clone https://github.com/Emanuelrestrepo22/selenium-py-POM.git

Paso 2: Crear el Entorno Conda
conda create -n selenium-env python=3.8
conda activate selenium-env

Paso 3: Instalar las Dependencias
pip install -r requirements.txt

Paso 4: Configurar el Archivo .env
⚠ IMPORTANTE: El archivo .env no está incluido por seguridad.
Debes crearlo manualmente en la raíz del proyecto con contenido como:
BASE_URL=https://www.saucedemo.com
USER_NAME=standard_user
PASSWORD=secret_sauce

Paso 5: Seleccionar el Intérprete en VSCode
1. Abre Ctrl + Shift + P.
2. Selecciona Python: Select Interpreter.
3. Elige el entorno creado (selenium-env).

Paso 6: Ejecutar Pruebas con Pytest
pytest -v --html=report.html --self-contained-html

Paso 7: Ejecutar Escenarios BDD con Behave
behave features/

Paso 8: Ver Resultados de Pruebas en VSCode
✅ Usa el Test Explorer de VSCode (icono ⚡) para debuggear, ejecutar y ver el estado de cada test.
✅ Si un test falla, asegúrate de revisar los logs y verificar las configuraciones del .env.

Paso 9: Opcional — Ver Versión de Selenium
python -c "import selenium; print(selenium.__version__)"

Paso 10: Prepararte para CI/CD
✅ Ajusta los archivos sanity.yml y regression.yml SOLO en la ruta de los tests.
✅ No borres ni modifiques configuraciones críticas de pipeline.

📢 Notas Finales
✅ Este proyecto combina lo mejor de Pytest (para asserts rápidos) y Behave (para BDD con Gherkin).
✅ Aplica Page Object Model (POM) para mantener el código limpio, reutilizable y mantenible.
✅ Asegúrate de mantener actualizadas las dependencias y las rutas de los tests para evitar fallas en CI/CD.

🤝 Contribuciones
Si quieres colaborar:
1. Haz un fork.
2. Crea una nueva rama (git checkout -b feature/NuevaFuncionalidad).
3. Haz commit de tus cambios.
4. Abre un Pull Request.

📌 Conéctate conmigo
Correo: emadavresgar@icloud.com
LinkedIn: linkedin.com/in/emanuelrestrepo
GitHub: github.com/Emanuelrestrepo22
Instagram: @emanuelrestrepo
Instagram Personal: @_restrepoema

⭐ ¡Si te gusta este proyecto, no olvides darle un ⭐ en GitHub! 🚀
"""


