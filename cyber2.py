from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do navegador
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()

try:
    # Navegar até a aba com o frame
    print("Acessando o frame...")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Single Iframe")))
    driver.find_element(By.LINK_TEXT, "Single Iframe").click()

    # Mudar para o frame
    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "singleframe")))
    input_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

    # Escrever no campo usando JavaScript para ser mais rápido
    driver.execute_script("arguments[0].value='Hello, this is Leonardo testing!';", input_box)

    # Verificação para confirmar a escrita
    assert "Hello, this is Leonardo testing!" == input_box.get_attribute('value'), "Texto não foi inserido corretamente"
    print("Teste de escrita em frame: PASSOU")

except Exception as e:
    print(f"Ocorreu um erro durante o teste: {e}")

finally:
    # Manter o navegador aberto
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
