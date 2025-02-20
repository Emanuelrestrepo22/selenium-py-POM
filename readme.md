<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![vscode-logo]][vscode-site] [![selenium-logo]][selenium-site] [![python-logo]][python-site] [![behave-logo]][behave-site]

<h1 align="center">🧪 Testing Automation: 🐍 Selenium 4.5 + Behave</h1>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://user-images.githubusercontent.com/91127281/200486232-5697197c-0541-4496-a487-bc720f234a1b.png" alt="Logo" width="" height="270">
  </a>

<h2 align="center">🧪 SELENIUM-PYTHON 🧪</h2>

  <p align="center">
    Selenium + Pytest + Behave (Gherkin) en VSCode
    <br />
    <a href="https://github.com/Emanuelrestrepo22/selenium-python"><strong>Explora la documentación »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Emanuelrestrepo22/selenium-python/blob/main/Tests/start/test_demo.py">Ver Demo</a>
  </p>
</div>

---

# 🌟 Sobre este Proyecto

Hola, soy **Emanuel Restrepo**, un apasionado del testing y la automatización de pruebas con **Selenium y Python**. Creé este proyecto como una forma de demostrar mis habilidades en **QA Automation**, mejorar continuamente y compartir conocimiento con la comunidad. Si eres **reclutador, equipo de trabajo o entusiasta de la automatización**, aquí encontrarás una implementación robusta y escalable de pruebas automatizadas.

Este repositorio combina **Selenium, Pytest y Behave (Gherkin)**, siguiendo buenas prácticas y estándares de la industria para automatizar la interacción con aplicaciones web. Es ideal para aquellos que buscan aprender sobre **automatización de pruebas con Selenium y POM (Page Object Model)**.

📌 **¿Por qué este proyecto?**
- Para demostrar habilidades en **QA Automation**.
- Para construir un framework de pruebas reutilizable y escalable.
- Para ayudar a otros testers y desarrolladores a iniciarse en la automatización.
- Para mostrar mi crecimiento y experiencia en el campo del testing.

---

## 🚀 Cómo Empezar

### **1️⃣ Pre-requisitos**
- Tener instalado **Anaconda** en la PC.
- Confirmar su instalación ejecutando:
  ```sh
  conda --version
  ```
- Configurar la variable de entorno en Windows: `C:\Users\Username\anaconda3`.

### **2️⃣ Clonar el Proyecto**
```sh
git clone https://github.com/Emanuelrestrepo22/selenium-python.git
```

### **3️⃣ Configurar el Entorno en VS Code**
1. Abrir **Command Palette** en VSCode (`Ctrl+Shift+P`).
2. Seleccionar `Python: Create Environment`.
3. Elegir `Conda` y la versión recomendada de Python.
4. Esperar a que se cree el entorno `.conda`.
5. Para activar el entorno:
   ```sh
   conda activate <full_path_env>
   ```

### **4️⃣ Instalar Dependencias**
```sh
pip install -r requirements.txt
```

### **5️⃣ Ejecutar Pruebas**
Para correr los tests automatizados:
```sh
pytest -v --html=report.html --self-contained-html
```

---

## 🏗️ Estrategia de Pruebas y Diseño

### 🔹 **Buenas Prácticas y Normativas**
1. **Nomenclatura correcta** para los archivos de prueba:
   ```sh
   test_{GXID}_{StoryShortName}.py  # Ejemplo: test_GX50_AgregarItemsAlCart.py
   ```
2. **Ubicación de los test suites** en el directorio correcto: `tests/coverage/`.
3. **Evitar el uso de fixtures como Page Object Model (POM)**.
4. **Uso de comandos Cypress** solo si se aplican correctamente.
5. **Aplicación estricta del patrón de diseño POM**.
6. **Uso correcto del CI Pipeline (sanity.yml y regression.yml)**.
7. **Revisión del diseño de los archivos Gherkin y Step Definitions en Behave**.

---

## 📌 Conéctate conmigo
Si te interesa mi trabajo o deseas colaborar, ¡contáctame!

📩 **Correo:** emadavresgar@icloud.com  
💼 **LinkedIn:** [linkedin.com/in/emanuelrestrepo](https://www.linkedin.com/in/emanuelrestrepo/)  
🐍 **GitHub:** [github.com/Emanuelrestrepo22](https://github.com/Emanuelrestrepo22)  
📸 **Instagram:** [@emanuelrestrepo](https://www.instagram.com/emanuelrestrepo/)  
📸 **Instagram Personal:** [@_restrepoema](https://www.instagram.com/_restrepoema/)  
💬 **Slack (Upex Galaxy):** [upexgalaxy.slack.com](https://upexgalaxy.slack.com/team/U055Q8W9N66)  

---

Si te gustó este proyecto, ⭐ ¡dale un star en GitHub! 🚀
