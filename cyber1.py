from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do navegador
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

# Esperar até que o formulário esteja carregado
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
)

# Preencher o formulário de registro
first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name.send_keys("Leonardo")
last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name.send_keys("Gatti")
address = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
address.send_keys("Rua Exemplo, 123")
email = driver.find_element(By.XPATH, "//input[@type='email']")
email.send_keys("leonardo@example.com")
phone = driver.find_element(By.XPATH, "//input[@type='tel']")
phone.send_keys("11999999999")
male_gender = driver.find_element(By.XPATH, "//input[@value='Male']")
male_gender.click()
cricket_hobby = driver.find_element(By.ID, "checkbox1")
cricket_hobby.click()
language_dropdown = driver.find_element(By.ID, "msdd")
language_dropdown.click()

# Submeter o formulário
submit_button = driver.find_element(By.ID, "submitbtn")
submit_button.click()

# Verificações
assert "Leonardo" == first_name.get_attribute('value'), "Nome não corresponde"
assert "Gatti" == last_name.get_attribute('value'), "Sobrenome não corresponde"
assert "leonardo@example.com" == email.get_attribute('value'), "Email não corresponde"
assert "11999999999" == phone.get_attribute('value'), "Telefone não corresponde"

print("Teste de preenchimento do formulário: PASSOU")

# Aguardar e fechar o navegador manualmente
input("Pressione Enter para fechar o navegador...")
driver.quit()




