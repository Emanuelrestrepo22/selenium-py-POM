Feature: Login en la plataforma (https://www.saucedemo.com/)

  Background:
    Given que el usuario está en la página de login

  Scenario: Usuario inicia sesión con credenciales válidas
    When ingresa su usuario desde el archivo .env
    And presiona el botón de login
    Then debería ver el mensaje de bienvenida "Products" en la página de lista de productos

  Scenario: Usuario intenta iniciar sesión con credenciales incorrectas
    When ingresa un usuario incorrecto y una contraseña incorrecta
    And presiona el botón de login
    Then debería ver el mensaje de error "Epic sadface: Username and password do not match any user in this service"
