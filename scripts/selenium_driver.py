from selenium.webdriver.chrome.webdriver import WebDriver

class Exceptions(Exception):
    ...
    
def lastWebDriver(nameFolder : str = None):
    """Localiza pastas das versões do Webdriver e retorna a versão de número mais alto."""
    import os

    nameFolder = nameFolder or fr"{os.getcwd()}\webDriver"
    folders = [int(a) for a in os.listdir(nameFolder)]

    return max(folders)

def pathDownload():
    """ Verifica se existe a pasta Downloads para uso do WebDriver, caso não exista ela será criada.""" 
    from os.path import exists
    from os import makedirs, getcwd
    
    if exists("Downloads"):
        return fr"{getcwd()}\Donwloads"
    else:
        makedirs("Downloads")
        return fr"{getcwd()}\Donwloads"

def configChromeDriver(webVisible : bool = True , filePathDownload : str = None, filePathWebDriver: str = None) -> WebDriver:
    """
    Configure o seu Chrome Driver:
    - webVisible ==> Por padrão True para ocultar o webDriver.
    - filePathDownload ==> Por padrão será criado uma pasta Downloads na raiz do projeto, caso não seja informado uma pasta para envio dos downloads ("nameFolder\\folderDownload").
    - filePathWebDriver ==> Informar o endereço completo, inclusive ("nameFolder\\91\\chromedriver.exe").
        Por padrão é utilizado a pasta raiz (webDriver), caso ela não exista, cria-la e colocar a pasta do driver nomeada com o numero da versão.
    """
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from os import getcwd
    
    filePathDownload = filePathDownload or pathDownload()
    filePathWebDriver = filePathWebDriver or fr"{getcwd()}\webDriver\{lastWebDriver()}\chromedriver.exe"
    
    options = Options()
    options.headless = webVisible
    prefs = {"download.default_directory": filePathDownload}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--lang=pt")
    
    return webdriver.Chrome(executable_path=filePathWebDriver, options=options)

def check_exists_elements(wb, method, element):
    """ Verifica se existe o elemento dentro da DOM HTML. Sempre informar se a busca será por (id, name, xpath ou css) e o valor da tag. """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    
    try:
        wb.find_element_by_class_name
        if method == 'id':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.ID,element)))
            wb.find_element_by_id(element)
        elif method == 'name':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.NAME,element)))
            wb.find_element_by_name(element)
        elif method == 'xpath':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.XPATH,element)))
            wb.find_element_by_xpath(element)
        elif method == 'class_name':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.CLASS_NAME,element)))
            wb.find_element_by_class_name(element)
        elif method == 'css_selector':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.CSS_SELECTOR,element)))
            wb.find_element_by_css_selector(element)
        elif method == 'link_text':
            WebDriverWait(driver=wb, timeout=30).until(EC.presence_of_element_located((By.LINK_TEXT,element)))
            wb.find_element_by_link_text(element)
        else:
            return False
        return True
    except Exception:
        raise Exceptions(method)