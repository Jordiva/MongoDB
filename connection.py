import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.jvalldaur

crear_colection_USUARIS = db.USUARIS
crear_colection_PACIENTS = db.PACIENTS
crear_colection_METGES = db.METGES

xls = pd.ExcelFile('Tasca3.xlsx')
df1 = pd.read_excel(xls, 'USUARIS')
df2 = pd.read_excel(xls, 'VISITES')
df3 = pd.read_excel(xls, 'HORARIS')

dt1_Usuaris = df1.to_dict(orient="records")
dt2_visites= df2.to_dict(orient="records")
dt3_Horaris = df3.to_dict(orient="records")

cols = [0]
a= pd.read_excel(xls, 'USUARIS' , usecols=cols )
ids_temporalsTots = a.to_dict(orient="records")

id_temporal_pacient = []


for row in dt1_Usuaris:
        
    cognoms = row['Cognoms,_i_Nom'].split(',')    
    
    _id = crear_colection_USUARIS.insert_one({
        'id_temporal': row['id_temporal'],
        'DNI': row['DNI'],
        'login': row['login'],
        'Sexe': row['Sexe'],
        'Nom': cognoms[1],
        'Cognoms': cognoms[0],
        'Data_Naixement': row['Data_Naixement'],
        'Adreça': row['Adreça'],
        'Població': row['Població'],
        'CP': row['CP'],
        'Província': row['Província'],
        'País': row['País']
    })
    
    if type(row["Especialitat"]) != float:
        crear_colection_METGES.insert_one({
            '_id': _id.inserted_id,
            'id_temporal': row['id_temporal'],
            'Especialitat': row['Especialitat'],
            'Num_colegiat': row['Num_colegiat']
    })
    
    if type(row["Mutua"]) != float:
        crear_colection_PACIENTS.insert_one({
            '_id': _id.inserted_id,
            'id_temporal': row['id_temporal'],
            'Mutua': row['Mutua'],
            'Num_mutualista': row['Num_mutualista']
    })

for row in dt2_visites: 
    crear_colection_METGES.update_one(
        { 'id_temporal': row['id_temporal_metge']},
        {'$push': {
            'agenda': {
                'moment_visita': datetime.strptime(row['Moment_visita'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                'id_temporal_pacient': row['id_temporal_pacient'],
                'realitzada': True if row['Realitzada'] == 's' else False,
                'informe': row['Informe'] 
            }
        }}
    )



for row in dt3_Horaris:
    crear_colection_METGES.update_one(
        {'id_temporal': row['id_temporal_metge']},
        {'$push': {
                'horaris': {
                    'dilluns': True if row['Dilluns'] == 's' else False,
                    'dimarts': True if row['Dimarts'] == 's' else False,
                    'dimecres': True if row['Dimecres'] == 's' else False,
                    'dijous': True if row['Dijous'] == 's' else False,
                    'divendres': True if row['Divendres'] == 's' else False,
                    'dissabte': True if row['Dissabte'] == 's' else False,
                    'inici_horari': row['Inici Horari'].strftime('%H:%M:%S'),
                    'fi_horari': row['Fi Horari'].strftime('%H:%M:%S')
                }
            
        }}
    )



crear_colection_METGES.update_many({}, {'$unset': {'id_temporal': 1}})
crear_colection_PACIENTS.update_many({}, {'$unset': {'id_temporal': 1}})
crear_colection_USUARIS.update_many({}, {'$unset': {'id_temporal': 1}})


