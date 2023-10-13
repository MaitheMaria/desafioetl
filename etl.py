import pandas as pd

df = pd.read_csv('desafioetl.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests
import json

def get_user(id):
  response = requests.get(f'https://sdw-2023-prd.up.railway.app/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

import requests
import json

def get_user(id):
    response = requests.get(f'https://sdw-2023-prd.up.railway.app/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]


for user in users:
    if user['account']['balance'] > 0:
        user['status'] = 'Ativo'
    else:
        user['status'] = 'Inativo'

print(json.dumps(users, indent=2))


import pandas as pd

# Supondo que 'users' seja a lista de usuários transformados
df = pd.DataFrame(users)

# Salvar como CSV
df.to_csv('dados_transformados.csv', index=False)
