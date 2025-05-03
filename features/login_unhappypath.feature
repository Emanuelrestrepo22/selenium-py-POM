Feature: Login fallido en la plataforma (https://www.saucedemo.com/)

  Background:
    Given que el usuario está en la página de login

  Scenario: Usuario intenta iniciar sesión con credenciales incorrectas
    When ingresa un usuario incorrecto y una contraseña incorrecta
    And presiona el botón de login
    Then debería ver el mensaje de error "Epic sadface: Username and password do not match any user in this service"
