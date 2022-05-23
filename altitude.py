import csv
import requests


rows=[]

with open('sismos.csv','r') as file:
    arquivo_lido = csv.reader(file)
    header= next(arquivo_lido)
    for row in arquivo_lido:
        rows.append(row[3:5]) #seleciona as colunas que de lat e long
    

    for row in rows:
        lat= row[0]
        long= row[1]

        response = requests.get('https://api.open-elevation.com/api/v1/lookup?locations='+str(lat)+','+str(long))
        response = response.json()

        elevation=(response['results'][0]['elevation'])
        row.append(elevation)

    with open('saída.csv','w', newline="") as saida:
        escrever= csv.writer(saida)
        header.insert(5,'Altitude') #insere o cabeçalho
        escrever.writerow(header[3:6]) #insere o cabeçalho
        escrever.writerows(rows)

