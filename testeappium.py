from appium import webdriver
from appium.options.android import UiAutomator2Options

# Configurações do servidor Appium
server = 'http://127.0.0.1:4723'

# Definindo as capacidades usando UiAutomator2Options
options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "Gatti"
options.platformVersion = "12"
options.appPackage = "com.kwai.video"
options.appActivity = "com.yxcorp.gifshow.tiny.TinyLaunchActivity"
options.noReset = True

# Iniciando a sessão com o Appium
driver = webdriver.Remote(command_executor=server, options=options)

# Seu código de automação começa aqui
print("Conexão bem-sucedida com o Appium!")













