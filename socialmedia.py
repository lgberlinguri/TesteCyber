from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Lista de contas (email, senha e URL da publicação no Kwai)
accounts = [
    {"email": "lmontblanc@proton.me", "password": "montblanc0109", "url": "https://k.kwai.com/p/7C54iQma"},
    {"email": "silvajoao1980@proton.me", "password": "joao123456", "url": "https://k.kwai.com/p/7C54iQma"},
    # Adicione mais contas conforme necessário
]

# Inicializar o WebDriver (usando Chrome, por exemplo)
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# Configuração do WebDriver
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Testando o acesso a uma página
driver.get("https://www.google.com")
print("ChromeDriver está funcionando!")
driver.quit()


for account in accounts:
    email = account['email']
    password = account['password']
    url = account['url']

    # Abrir a página de login do Kwai
    driver.get("https://www.kwai.com/login")

    # Realizar login (ajuste os seletores conforme necessário)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    time.sleep(3)  # Aguarde carregar

    # Navegar até a URL da publicação
    driver.get(url)

    # Simular o clique (ajuste o seletor conforme necessário)
    like_button = driver.find_element(By.CLASS_NAME, "like-button")
    like_button.click()

    time.sleep(2)  # Pausa para garantir que o clique foi realizado antes de passar para o próximo

# Fechar o navegador após processar todas as contas
driver.quit()
