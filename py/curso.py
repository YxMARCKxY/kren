from lector import id_curso
import json

with open('data.json') as file:
    data = json.load(file)
    for client in data['clients']:
        idCurso = json.dumps(client['age'])

id_curso(idCurso)