import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



class digitacao:
    def __init__(self, tempo, aguardar):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.tempo = tempo
        self.aguardar = aguardar
        self.wait = WebDriverWait(self.driver, self.tempo)
        pass

    def verifica_hora(self, hora):
        if hora >= '6':
            print('hora')

    def preenche_str(self, element, info):
        try:
            self.driver.find_element(By.XPATH,element).send_keys(info)
            return True
        except:
            return False
    
    def preenche_int(self, element, info, info2=' '):
        try:
            elemento = WebDriverWait(self.driver, self.aguardar).until(
                EC.presence_of_element_located((By.XPATH, element))
            ) 
            text = info , info2
            elemento.click()
            for z in text:
                action = ActionChains(self.driver) 
                time.sleep(0.1)
                action.send_keys(z)
                action.perform()

            time.sleep(self.tempo)
            return True
        except: 
            return False 

    def iniciar(self):
        try:
            self.driver.get('http://54.94.101.28')
            return True
        except:
            return False
    
    def login_seg(self, login, senha):
        try:
            self.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/form/div[1]/div/div/input'
            ).send_keys(login)
            self.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/form/div[2]/div/div/input'
            ).send_keys(senha)
            self.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/form/div[3]/button'
            ).click()
            return True
        except:
            return False
    def operacao(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/div/div/div[4]/div/div/div[2]')))
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div[3]/span').click()
            self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[3]/div/div').click()
            return True
        except:
            return False
    def preenche_sexo(self,sexo):
        if sexo == 'Masculino':
            time.sleep(self.tempo)
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div/div/div'
            ).click()
        else:
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div/div/div'
            ).click()
            time.sleep(self.tempo)
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div/div/div/div[2]/div[1]'
            ).click()
    
            

    def clicar_campo(self, element):
        self.driver.find_element(By.XPATH,element).click()

    def inserir(self):
        try:
            try:
                time.sleep(self.aguardar)
                self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/h2')))
                self.driver.find_element(By.XPATH,'/html/body/div[2]/div/i').click()
            except:
                time.sleep(self.aguardar)
                self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/h4')))
                self.driver.find_element(By.XPATH,'/html/body/div[2]/div/i').click()
            return True
        except:
            return False
    
    def limpar(self):
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[1]/div/div/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div/div/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[1]/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div/div/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[3]/div/input').clear()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div[1]/div/input').clear()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div[3]/div/div/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/input').clear()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/input').clear()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/div[3]/input').clear()