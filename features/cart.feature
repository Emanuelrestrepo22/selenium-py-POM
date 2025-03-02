Feature: Gestión del Carrito de Compras

  Background:
    Given que el usuario ha iniciado sesión y está en la página de lista de productos

  Scenario: Agregar productos al carrito
    When el usuario añade 5 productos al carrito
    Then debería ver el número 5 en el icono del carrito

  Scenario: Remover productos del carrito
    Given que el usuario ha añadido 5 productos al carrito
    When el usuario remueve 2 productos del carrito
    Then debería ver el número 3 en el icono del carrito
