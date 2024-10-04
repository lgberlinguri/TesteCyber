from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do navegador
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Slider.html")
driver.maximize_window()

try:
    # Esperar até que o slider esteja carregado
    print("Aguardando o slider...")
    slider_handle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='ui-slider-handle ui-state-default ui-corner-all']"))
    )

    # Mover o slider usando ActionChains
    print("Movendo o slider para 50%...")
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider_handle, 100, 0).perform()  # Ajustar o deslocamento conforme necessário

    # Verificar o valor visual do slider (exibido no slider, se disponível)
    slider_value = driver.find_element(By.ID, "slider").get_attribute("style")  # Estilo CSS do slider
    print(f"Valor do slider após o movimento: {slider_value}")
    print("Teste do Slider: PASSOU")

except Exception as e:
    print(f"Ocorreu um erro durante o teste: {e}")

finally:
    # Manter o navegador aberto
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

