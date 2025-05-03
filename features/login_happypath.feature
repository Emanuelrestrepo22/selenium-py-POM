Feature: Login exitoso en la plataforma (https://www.saucedemo.com/)

  Background:
    Given que el usuario está en la página de login

  Scenario: Usuario inicia sesión con credenciales válidas
    When ingresa su usuario desde el archivo .env
    And presiona el botón de login
    Then debería ver el mensaje de bienvenida "Products" en la página de lista de productos
