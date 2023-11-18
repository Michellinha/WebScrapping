import pandas as pd
from selenium import webdriver

#Permitindo o uso do teclado
from selenium.webdriver.common.keys import Keys

#Permitindo a seleção de elementos
from selenium.webdriver.common.by import By

#Gerencia os Chromes Drivers disponíveis para acessarmos o mais atualizado
from webdriver_manager.chrome import ChromeDriverManager

#Instalar a versão ais atualizada com Chrome Driver
from selenium.webdriver.chrome.service import Service
import time

from bs4 import BeautifulSoup
import requests
import re


#opcional
from selenium.webdriver.chrome.options import Options
chrome_options = Options

#Inicializando o driver Selenium
#driver = webdriver.Chrome

#from webdriver_manager.chrome import ChromeDriverManager
navegador  = webdriver.Chrome()
navegador.get('https://kavak.com/br/seminovos')

time.sleep(5)


navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#Aguarde um tepo para que a página seja totalmente carregada, se necessário
time.sleep(10)

#Encontre os elementos desejados usando seletores do Selenium
classe_produto = navegador.find_elements(By.CLASS_NAME, "title") [1:]


# click on button with the id "login-btn"
button = navegador.find_element(By.CLASS_NAME, "paginator-btn-primary")
button.click()

lista_produto = []

#Itere sobre os elementos encontrados e extorna os dados
for produto in classe_produto:
  lista_produto.append(produto.text)

print("\n################## Lista de Produtos ######################\n")
print(lista_produto)

classe_preco = navegador.find_elements(By.CLASS_NAME,'price')
lista_preco = []

for preco in classe_preco:
  lista_preco.append(preco.text)
  
print("\n################## Lista de Preços ######################\n")
print(lista_preco)
 #trouxe preço á vista e parcelado

classe_preco = navegador.find_elements(By.CLASS_NAME,'price')
lista_preco = []

for i in range(0,len(classe_preco),2):
  lista_preco.append(preco.text)
  
print("\n################## Lista de Preços ######################\n")
print(lista_preco)
  #retorna apenas o preço à vista

classe_preco = navegador.find_elements(By.CLASS_NAME,'price')
lista_precos = []

for preco in classe_preco:
  lista_precos.append(preco.text.replace('R$', " ").strip)

print("\n################## Lista de Preços ######################\n")
print(lista_precos)
  #trata o cirão e o espaço

#Encontre os elementos desejados usando seletores do Selenium
classe_detalhes = navegador.find_elements(By.CLASS_NAME,'subtitle')

#Crie listas vazias para armazenar dados
lista_detalhes = []

#Itere sobre os elementos encontrados e estraia os dados:
for detalhes in classe_detalhes:
  lista_detalhes.append(detalhes.text.strip())
  
print("\n################## Lista de Detalhes ######################\n")
print(lista_detalhes)

#Encerre o driver do Selenium após extrair as informações necessárias
navegador.quit()

#Crie um Dataframe no Pandas com as informações extraídas
df = pd.DataFrame({'Produto':lista_produto},{'Preco': lista_precos}, {'Detalhes': lista_detalhes})

print("\nImprimindo Dataframe:\n")
print(df)

#Salve o Dataframe com um arquivo Excel

df.to_excel("Dados1.xlsx")

df.to_excel('Dados2.xlsx', index=False)