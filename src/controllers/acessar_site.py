from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

class Forms:
    """
        Classe responsável, pelo formulário, nela temos os métodos:
        xpaths -> que guarda todos os xpaths do formulário;
        preenche_forms -> que abre o formulário e preenche os dados.
    """
    def __init__(self, url_site:str) -> None:
        self.url = url_site
        self.chromedriver = chromedriver_autoinstaller.install()  
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--lang=pt-BR')
        self.chrome_options.add_argument('disable-infobars')
        self.chrome_options.add_argument('--log-level=3')
    
    def xpaths(self) -> dict:
        """
            Método que armazena um dicionário com xpaths do forms.

        Returns:
            dict: etorna um dicionário com xpaths do forms
        """
        XPATH = {
            'xp_email': '//*[@type="email"]', 
            'xp_nome': '//*[@type="text"]', 
            'xp_niver': '//*[@type="date"]',
            'xp_genero': '//*[@class="bzfPab wFGF8"]//span[text()="{}"]',
            'xp_sobre': '//*[@class="KHxj8b tL9Q4c"]',
            'xp_next': '//span[text()="Próxima"]',
            'xp_serie': '//*[@aria-describedby="i2 i3"]',
            'xp_escolher': '//span[text()="Escolher"]',
            'xp_estilo_music': '//*[@class="OA0qNb ncFHed QXL7Te"]//span[text()="{}"]',
            'xp_filme': '//*[@aria-describedby="i10 i11"]',
            'xp_enviar': '//span[text()="Enviar"]',
            'xp_again':  '//a[text()="Enviar outra resposta"]'   
        }
        return XPATH
        
    def preenche_forms(self,date:list) -> str:
        """
            Método responsável por acessar e preencher o formulário;        

        Args:
            date (list): recebe uma lista de dicionário.

        Returns:
            str: retorna se deu tudo certo ou deu erro.
        """
        try:
           
            XPATH = self.xpaths()
            time.sleep(2)
            driver = webdriver.Chrome(self.chromedriver,options=self.chrome_options)
            driver.get(self.url)
            #driver.maximize_window()

            for dados in date:
                time.sleep(3)
                driver.find_element(By.XPATH,XPATH['xp_email']).send_keys(dados['email'])
                driver.find_element(By.XPATH,XPATH['xp_nome']).send_keys(dados['nome'])
                driver.find_element(By.XPATH,XPATH['xp_niver']).send_keys(dados['niver'].strftime('%d/%m/%Y'))
                driver.find_element(By.XPATH, XPATH['xp_genero'].format(dados['genero'])).click()
                driver.find_element(By.XPATH,XPATH['xp_sobre']).send_keys(dados['sobre'])
                driver.find_element(By.XPATH,XPATH['xp_next']).click()
                time.sleep(1)
                driver.find_element(By.XPATH,XPATH['xp_serie']).send_keys(dados['serie'])
                driver.find_element(By.XPATH,XPATH['xp_escolher']).click()
                time.sleep(1)
                driver.find_element(By.XPATH,XPATH['xp_estilo_music'].format(dados['estilo_music'])).click()
                time.sleep(1)
                driver.find_element(By.XPATH,XPATH['xp_filme']).send_keys(dados['filme'])
                time.sleep(1)
                driver.find_element(By.XPATH,XPATH['xp_enviar']).click()
                time.sleep(1)
                driver.find_element(By.XPATH,XPATH['xp_again']).click()
                time.sleep(2)
            return 'Tudo certo'
        except:
            return "Error"
            