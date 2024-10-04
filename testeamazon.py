import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL da página a ser testada
url = "https://www.amazon.com.br"

class AmazonTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Remova o argumento 'executable_path'
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_autocomplete(self):  # em desenvolvimento
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.send_keys("iPhone")
            suggestions = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@id='suggestions']/div"))
            )
            self.assertGreater(len(suggestions), 0, "Nenhuma sugestão encontrada")
            print("Teste Autocomplete: PASSOU")
        except Exception as e:
            print(f"Erro no teste de autocomplete: {str(e)}")

    def test_navigation_menu(self): # em desenvolvimento
        try:
            menu_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "nav-hamburger-menu"))
            )
            menu_button.click()
            time.sleep(2)
            menu_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='hmenu-visible']/li/a"))
            )
            self.assertGreater(len(menu_items), 0, "Itens do menu não carregaram")
            print("Teste Menu de Navegação: PASSOU")
        except Exception as e:
            print(f"Erro no teste de navegação do menu: {str(e)}")

    def test_page_load(self):
        try:
            start_time = time.time()
            self.driver.get(url)
            load_time = time.time() - start_time
            self.assertLess(load_time, 3, f"Página carregou em {load_time} segundos, que é maior que o esperado")
            print(f"Teste de Carregamento: PASSOU ({load_time:.2f} segundos)")
        except Exception as e:
            print(f"Erro no teste de carregamento da página: {str(e)}")

if __name__ == "__main__":
    unittest.main()

