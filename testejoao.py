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

# Localizar e clicar no botão 'Continuar com Google'
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.video:basicid/google_login_btn")').click()

# Esperar um tempo para carregar a conta Google e fazer login automaticamente
time.sleep(10)

# Navegar até a publicação através da URL
driver.get("https://k.kwai.com/p/7C54iQma")
time.sleep(3)

# Localizar e clicar no botão de curtir
like_button = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageView").descriptionContains("curtir")')
like_button.click()

# Manter a página aberta por 1 minuto e 30 segundos para interação
time.sleep(90)

# Fechar a sessão do driver
driver.quit()

