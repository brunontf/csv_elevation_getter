import csv
import requests


rows=[]
coluna_lat=3  #lembrar que a primeira coluna é a "0", a primeira necess. tem que ser LATITUDE
coluna_long=4
nome_do_arquivo = 'sismos.csv'

with open(nome_do_arquivo,'r') as file:
    arquivo_lido = csv.reader(file)
    header= next(arquivo_lido)
    for row in arquivo_lido:
        rows.append(row[coluna_lat:coluna_long+1]) #seleciona as colunas que de lat e long
    

    for row in rows:
        lat= row[0]
        long= row[1]

        response = requests.get('https://api.open-elevation.com/api/v1/lookup?locations='+str(lat)+','+str(long))
        response = response.json()

        elevation=(response['results'][0]['elevation'])
        row.append(elevation)

    with open('saída.csv','w', newline="") as saida:
        escrever= csv.writer(saida)
        header.insert(coluna_long+1,'Altitude') #insere o cabeçalho
        escrever.writerow(header[coluna_lat:coluna_long+2]) #insere o cabeçalho
        escrever.writerows(rows)
print("ACABOU! \n \nou não")
