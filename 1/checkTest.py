from zeep import Client, Settings
import yaml


with open ('addr.yaml') as f:
    wsdl = yaml.safe_load(f)['wsdl']    

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings= settings)

def checkText(word):
    return client.service.checkText(word)[0]['s']

""" с использованием pytest наптсать тест операции checkTest SOAP API
(адрес wdsl). Тест должен использовать DDT и проверять наличие определенного
верного слова в списке предложенных исправлений к определенному 
неверному слову. Слова должны быть заданы через фикстуры conftest.py
адрес wdsl должен быть вынесен в config.yaml. Методы работы с 
SOAP должны быть вынесены в отдельную библиотеку"""