import pandas as pd
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def rand_time():
    """
    Gera valores não inteiros aleatorios em intervalos de 5.5 e 6.5 segundos,
    uma contramedida para que o sistema nao impeca a automacao.
    """
    random_time = time.sleep(random.uniform(5.5, 6.5))
    
    return random_time


def rand_short():
    """
    Gera valores não inteiros aleatorios em intervalos de 0.8 e 1.5 segundos,
    uma contramedida para que o sistema nao impeca a automacao.
    """
    random_short = time.sleep(random.uniform(0.8, 1.5))
    
    return random_short

# 1) importando a base da primeira etapa
df = pd.read_excel(r'1.2-Convênios_com_Atualização.xlsx')
df.columns = ['Convenio']
df['Convenio'] = df['Convenio'].astype(str)
# 2) Acesso ao sistema (na hora que estiver operacional)
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome() #options = options 
driver.get('https://www.santandernegocios.com.br/portaldenegocios/#/externo')
# encontrando campos de login e senha
rand_time()
driver.find_element_by_id('userLogin__input').send_keys(str(input('LOGIN (ctrl+c/ctrl+v): ')))  # login direto para teste
rand_short()
driver.find_element_by_id('userPassword__input').send_keys(str(input('SENHA (ctrl+c/ctrl+v): ')))  # senha direto para teste
driver.find_element_by_xpath('/html/body/app/ui-view/login/div/div/div/div/div[2]/div[3]/button[2]').click()  # entra
rand_time()
driver.find_element_by_xpath('//*[@id="header"]/div[4]/user-menu/div/div').click()
rand_time()
driver.find_element_by_xpath('//*[@id="header"]/div[4]/user-menu/div/nav/div/div[3]/ul/li[2]/a').click()
# Mudando de aba ao programa para continuar na outra aba
rand_time()

try:
    current = driver.current_window_handle
    after = driver.window_handles[1]
    driver.switch_to.window(after)
    rand_time()
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_j0_j1_DataListMenu_ctl03_LinkButton2"]').click()
    # acessando aba do tipo "hover/mouseover"
    rand_time()
    consulta_hover = driver.find_element_by_xpath('//*[@id="cph_Menu1n1"]/table/tbody/tr/td[1]/a')
    ActionChains(driver).move_to_element(consulta_hover).perform()
    # acessando submenu
    rand_time()
    aditivo_hover = driver.find_element_by_link_text('Consulta de Contrato Aditivo')
    ActionChains(driver).move_to_element(aditivo_hover).click().perform()

except NoSuchElementException:
    pass

finally:
    # preparando pagina para receber dados dos convenios CGR3.0
    driver.find_element_by_id('cph_j0_j1_UcCOMISSIONADO1_E_COD_CAMPO').clear()
    time.sleep(0.8)
    driver.find_element_by_id('cph_j0_j1_UcCOMISSIONADO1_E_COD_CAMPO').send_keys('30196' + Keys.ENTER)
    rand_short()
    driver.find_element_by_id('cph_j0_j1_UcPeriodoVig_E_DATAINI_CAMPO').clear()
    rand_short()
    driver.find_element_by_id('cph_j0_j1_UcPeriodoVig_E_DATAFIM_CAMPO').clear()
    rand_short()
    driver.find_element_by_id('cph_j0_j1_UcPeriodoAceite_E_DATAINI_CAMPO').clear()
    rand_short()
    driver.find_element_by_id('cph_j0_j1_UcPeriodoAceite_E_DATAFIM_CAMPO').clear()
    # CONFIGURAR CHECKBOX PARA "ATIVO" E "NOVO"
    # Tratando checkbox 'ativo'
    # Certificando desativacao de todos
    rand_short()
    if (driver.find_element_by_id('cph_j0_j1_ucSTATUS_CheckBoxList1_0').is_selected()) == True:
        driver.find_element_by_id('cph_j0_j1_ucSTATUS_CheckBoxList1_0').click()
    rand_short()
    if (driver.find_element_by_id('cph_j0_j1_ucSTATUS_CheckBoxList1_1').is_selected()) == True:
        driver.find_element_by_id('cph_j0_j1_ucSTATUS_CheckBoxList1_1').click()
    rand_short()
    if (driver.find_element_by_id('cph_j0_j1_ucSTATUSACEITE_CheckBoxList1_0').is_selected()) == True:
        driver.find_element_by_id('cph_j0_j1_ucSTATUSACEITE_CheckBoxList1_0').click()
    rand_short()
    if (driver.find_element_by_id('cph_j0_j1_ucSTATUSACEITE_CheckBoxList1_1').is_selected()) == True:
        driver.find_element_by_id('cph_j0_j1_ucSTATUSACEITE_CheckBoxList1_1').click()
    # Ativando 'ativo' e 'novo'
    driver.find_element_by_id('cph_j0_j1_ucSTATUS_CheckBoxList1_0').click()
    driver.find_element_by_id('cph_j0_j1_ucSTATUSACEITE_CheckBoxList1_0').click()
    
    for i in range(0, len(df)):

        try:
            id_box = 'cph_j0_j1_UcEmpregador1_E_COD_CAMPO'
            id_button = 'FIButton1_txt'
            element_1 = driver.find_element_by_id(id_box)
            element_2 = driver.find_element_by_id(id_button)

            element_1.clear()  # Limpa campo
            ActionChains(driver).move_to_element(
                element_1).click().perform()  # Seleciona campo
            element_1.send_keys(df['Convenio'][i])  # digita valor da lista
            ActionChains(driver).move_to_element(element_2).click().perform()
            element_2.click()

            time.sleep(random.uniform(8.5, 9.0))

        except NoSuchElementException:
            pass

        except StaleElementReferenceException:
            id_box = 'cph_j0_j1_UcEmpregador1_E_COD_CAMPO'
            id_button = 'FIButton1_txt'
            element_1 = WebDriverWait(driver, 240, poll_frequency = 400).until(EC.presence_of_element_located((By.ID, id_box)))
            element_2 = WebDriverWait(driver, 240, poll_frequency = 400).until(EC.element_to_be_clickable((By.ID, id_button)))

            element_1.clear()  # Limpa campo
            ActionChains(driver).move_to_element(element_1).click().perform()  # Seleciona campo
            element_1.send_keys(df['Convenio'][i])  # digita valor da lista
            ActionChains(driver).move_to_element(element_2).click().perform()
            element_2.click()

            time.sleep(random.uniform(8.5, 9.0))  # Para a conexão
            
            # Continua comandos depois daqui:
            # 1) Clicar no aditivos
            # 2) Dar o aceite "liberar Formalizacao"
            # 3) Tratar alerta "Aditivo aceito com sucesso"
            # 3) Retroagir data: data de inicio = dia anteiror e data final = dia atual
            # 4) Mudar marcacao de "Novo" para "Aceito" e clicar em continuar
            # 5) Clicar no aditivo
            # 6) Clicar para baixar o aditivo (arquivo PDF)
            # 7) Ler e captar os dados paraa um arquio CSV (cada convenio com sua regra)
            # 8) Salvar PDF e CSV na pasta "Documentos" localmente
            # 9) Nomear PDF e CSV
            # 10) Repetir todo o processo em cada aditivo de cada pagina
            
        except ElementNotInteractableException:
            pass
      
                
'''
        text_none = driver.find_element_by_id('cph_j0_j1_GRADITIVO').text
        text = 'Nenhum registro encontrado!'
        if text_none != text:
            convenio_update.append(unique[i])
'''

                

#ADICIONAR SOLICITACAO PARA USAR BASE CRIADA NA PRIMEIRA AUTOMAÇÃO [Y/N], PARA
#CASO FOR FAZER BUSCA APENAS PARA OS GESTORES NÃO SE UTILIZAR A BASE