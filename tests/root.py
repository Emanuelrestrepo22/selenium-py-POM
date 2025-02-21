import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.root import BASE_URL

#cargar var de entorno desde .env
load_dotenv()

def get_tests_root():
    #retorna la raiz del proyecto
    return os.path.dirname(__file__)

#obtener credenciales y  entorno de prueba desde .env 
TEST_ENV = os.getenv('TEST_ENV', 'QA').upper() #defaul used QA
PASSWORD = os.getenv('SWL_USERNAME')
USERNAME = os.getenv('USERNAME')

# Configuración de las URLs por ambiente
baseUrl = {
    'DEV': os.getenv('DEV_URL', 'https://www.saucedemo.com/'),
    'QA': os.getenv('QA_URL', 'https://www.saucedemo.com/'),
    'PROD': os.getenv('PROD_URL', 'https://www.saucedemo.com/')
}

BASE_URL = baseUrl.get(TEST_ENV, baseUrl['QA'])  # Si el entorno no está en la lista, usa QA