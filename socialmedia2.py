from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Lista de contas e URLs de publicações
accounts = [
    {"email": "user1@protonmail.com", "password": "senha1", "url": "https://kwai.com/post/123"},
    {"email": "user2@protonmail.com", "password": "senha2", "url": "https://kwai.com/post/456"},
    {"email": "user3@protonmail.com", "password": "senha3", "url": "https://kwai.com/post/789"},
    {"email": "user4@protonmail.com", "password": "senha4", "url": "https://kwai.com/post/101"},
    {"email": "user5@protonmail.com", "password": "senha5", "url": "https://kwai.com/post/112"},
]

# Loop para fazer login e interagir em cada publicação
for account in accounts:
    email = account['email']
    password = account['password']
    url = account['url']
    
    # Navegar até a página de login
    driver.get("https://kwai.com/login")
    time.sleep(2)  # Ajuste conforme a necessidade de carregamento
    
    # Preencher o formulário de login
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login_button").click()  # Ajuste o seletor conforme necessário
    time.sleep(5)  # Esperar a página carregar

    # Navegar até a URL da publicação
    driver.get(url)
    time.sleep(3)

    # Simular o clique no botão de curtir (ajuste o seletor conforme necessário)
    like_button = driver.find_element(By.CLASS_NAME, "like-button-classname")
    like_button.click()

    time.sleep(2)  # Pausa após a ação

# Fechar o navegador após processar todas as contas
driver.quit()
