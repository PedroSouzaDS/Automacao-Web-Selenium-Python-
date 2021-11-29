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

# 1) importacao e preparacao dos dados - solicitacao de gestores
# receber input manual
# coloca-lo em uma lista 
# transformar lista em dataframe
# juntar o dataframe da solicitacao de gestores com a base do update com solicitacao
#... dos gestores em primeiro lugar (preferencial)
#df_update = pd.read_excel(r'J:\03_TABELAS\01_Controle_Geral_de_Remuneração\NOVO CGR - Santander\1.2-Convênios_com_Atualização.xlsx', header=None, usecols=[0])
'''
SOLICITACAO DAS REGRAS DOS GESTORES, ADICIONAR NUMEROS A PRIORI E ESTABELECER UMA LISTA 
COM PRIORIDADE PARA ESTES CONVENIOS

PROBLEMAS: NAO CONSEGUINDO GERAR A LISTA COMPLETA COM AS SOLUCOES DOS GESTORES 
INPUTADAS MANUALMENTE, SALTAR ESTA PARTE E CONTINUAR NA BASE GERADA PELA PRIMEIRA AUTOMACAO

mng_list = []
mng_req = str(input('Solicitacao de gestores [y/n]? ' ))
while mng_req not in 'YyNn':
    print('Opcao indisponivel, digite Y/y ou N/n!')
    mng_req = str(input('Solicitacao de gestores [y/n]? ' ))
    
# caso opcao seja Yy
# se a opcao escolhida for Yy, entao solicita-se os numeros 
if mng_req in 'Yy':
    while True:
        n = int(input('Digite o convenio solicitado: '))
        q = str(input('Outro convenio [y/n]? '))
        if q in 'Nn':
            break
        while q not in 'YyNn':
            print('Opcao indisponivel, digite Y/y ou N/n!')
            q = str(input('Outro convenio [y/n]? '))
        mng_list.append(n)
        
print(mng_list)

ADICIONAR SOLICITACAO PARA USAR BASE CRIADA NA PRIMEIRA AUTOMAÇÃO [Y/N], PARA
CASO FOR FAZER BUSCA APENAS PARA OS GESTORES NÃO SE UTILIZAR A BASE
'''






            


    