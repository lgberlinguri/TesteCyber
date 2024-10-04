from appium import webdriver
import time

# Configuração do WebDriver para Appium
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Gatti',  # Substitua pelo nome do seu dispositivo
    'appPackage': 'com.kwai.video',  # Pacote do aplicativo Kwai
    'appActivity': 'com.kwai.video.homepage.HomeActivity',  # Atividade inicial do Kwai
    'noReset': True,  # Não reinicia o app entre as sessões de automação
    'automationName': 'UiAutomator2'
}

# Conectando ao servidor do Appium
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# A espera implícita é usada para aguardar a presença de elementos antes de interagir
driver.implicitly_wait(10)

# Navegar até a publicação através da URL (isso pode exigir ajustes adicionais)
# Substitua 'seu_link' pelo link específico que você quer interagir
driver.get("seu_link")
time.sleep(3)

# Localizar e clicar no botão de curtir, utilizando seletores atualizados conforme identificados
like_button = driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Curtir")')
like_button.click()

# Manter a página aberta por 1 minuto e 30 segundos para interação manual ou observação
time.sleep(90)

# Fechar a sessão do driver
driver.quit()
