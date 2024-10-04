from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuração do navegador
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()

try:
    # Esperar a página carregar completamente e verificar se o campo de datepicker está visível
    print("Aguardando o carregamento da página...")
    date_field1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "datepicker1"))
    )
    date_field2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "datepicker2"))
    )

    # Interagir com o primeiro campo de data usando JavaScript
    print("Interagindo com o primeiro campo de data...")
    driver.execute_script("arguments[0].value = arguments[1];", date_field1, "01/09/1980")

    # Interagir com o segundo campo de data usando JavaScript
    print("Interagindo com o segundo campo de data...")
    driver.execute_script("arguments[0].value = arguments[1];", date_field2, "01/09/1980")

    # Verificações e mensagem de status
    print("Verificando as entradas de data...")
    assert "01/01/1980" == date_field1.get_attribute('value'), "Data no primeiro campo não corresponde"
    assert "01/01/1980" == date_field2.get_attribute('value'), "Data no segundo campo não corresponde"
    print("Teste do Datepicker: PASSOU")

except Exception as e:
    print(f"Ocorreu um erro durante o teste: {e}")

finally:
    # Manter o navegador aberto
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
