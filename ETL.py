import requests
import json

# Função paara extrair os dados da API DummyJson
def extrair_dados(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao extrair os dados da API: {response.status_code}')

# Função para Carregar os dados e criar o arquivo.json
def load_data(data, path):
    id = data['id']
    # Dentro da pasta path criar um arquivo json com o nome do arquivo sendo 'id' o nome do arquivo.json
    with open(f'{path}/{id}.json', 'w') as file: # users/id.json
        json.dump(data, file) # salvar dados em formato JSON dentro de um arquivo.

# Links das API's
endpoint_user = 'https://dummyjson.com/users/'

i = 1 # contador
while True:
    data_users = extrair_dados(endpoint_user + str(i)) # 'https://dummyjson.com/users/str(i)'
    if data_users:
        load_data(data_users, 'users') # Carregando os dados esxtraidos da API dentro da pasta 'users'
    else: 
        print(f'Erro ao extrair os dados da API: {data_users}')
        break
    i+= 1