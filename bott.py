import os
import time
import re
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt

class newbot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Firefox()

    def climaTempo(self):
        try:

            site  = 'https://www.climatempo.com.br'
            self.driver.get(site)
            self.driver.implicitly_wait(20)

            i = 0
            while True:
                estado=11
                cidades = [70,217] 

                #11 = Minas Gerais
                #70 = Belo Horizonte, 217 = Contagem

                self.driver.find_element_by_xpath('//*[@id="momento-localidade"]').click()
                self.driver.find_element_by_xpath('/html/body/div[7]/select[1]/option[' + str(estado) + ']').click()
                self.driver.find_element_by_xpath('/html/body/div[7]/select[2]/option[' + str(cidades[i]) + ']').click()
                self.driver.find_element_by_xpath('//*[@id="btn-confirm-geo"]').click() 

                time.sleep(20)

                localidade = self.driver.find_element_by_xpath('//*[@id="momento-localidade"]').text
                temperatura = self.driver.find_element_by_xpath('//*[@id="momento-temperatura"]').text
                condicao = self.driver.find_element_by_xpath('//*[@id="momento-condicao"]').text
                sensacao = self.driver.find_element_by_xpath('//*[@id="momento-sensacao"]').text
                humidade = self.driver.find_element_by_xpath('//*[@id="momento-humidade"]').text
                pressao = self.driver.find_element_by_xpath('//*[@id="momento-pressao"]').text
                velocVento = self.driver.find_element_by_xpath('//*[@id="momento-vento"]').text
                ultimaAtualizacao = self.driver.find_element_by_xpath('//*[@id="momento-atualizacao"]').text

                dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print("Localidade: " + localidade)
                print("Temperatura: " + temperatura)
                print("Condição: " + condicao)
                print("Sensação Termica: " + sensacao)
                print("Humidade: " + humidade)
                print("Pressão: " + pressao)
                print("Velocidade do Vento: " + velocVento)
                print("Ultima Atualização Clima Tempo: " + ultimaAtualizacao)
                print("Data da Consulta: " + dat)
                print('-----------------------------')

                time.sleep(10)

                dados = localidade + ';' + temperatura + ';' + condicao + ';' + sensacao + ';' + humidade + ';' + pressao + ';' + velocVento  + ';' + ultimaAtualizacao + ';' + dat
                self.salvaDados(dados)

                i+=1
                if(i>1):
                    i=0
        except:
            self.driver.close()
            self.erro()


    def erro(self):
         self.climaTempo()

    def salvaDados(self, dados):
        datt = datetime.now().date().strftime("%Y-%m-%d")
        arquivo = open('C:/Users/rafael.dourado/Desktop/ClimaTempo/Dados - ' + datt + '.txt', 'a')
        arquivo.write(dados + '\n')
        arquivo.close()











        
        
