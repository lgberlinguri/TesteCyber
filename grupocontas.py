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

# Aguardar a presença dos elementos antes de interagir
driver.implicitly_wait(10)

# Entrar com a conta do Google logada previamente
# Simula a interação para chegar até o botão 'Alternar Conta'
driver.find_element_by_xpath('//android.widget.ImageView[contains(@content-desc,"Perfil")]').click()
time.sleep(2)  # Ajuste conforme a necessidade de tempo de resposta da interface

# Clicar em 'Configurações'
driver.find_element_by_android_uiautomator('new UiSelector().text("Configurações")').click()
time.sleep(1)

# Clicar em 'Alternar Conta'
driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.kwai.video.dfm_profile:id/wrapper"]/android.widget.LinearLayout/android.view.ViewGroup[9]').click()
time.sleep(1)

# Selecione a conta desejada, aqui você precisará definir como selecionar
# Por exemplo, sempre clicar na segunda conta listada
driver.find_element_by_android_uiautomator('new UiSelector().text("Segunda Conta")').click()
time.sleep(1)

# Navegar até a publicação específica - ajuste a URL conforme necessário
driver.get("https://k.kwai.com/p/7C54iQma")
time.sleep(90)  # Espera 1 minuto e 30 segundos na página

# Clicar no botão de curtir
driver.find_element_by_xpath('//android.view.View[@resource-id="pwa-share-new-container"]/android.view.View[4]/android.view.View[2]').click()
time.sleep(2)

# Fechar a sessão do driver
driver.quit()
