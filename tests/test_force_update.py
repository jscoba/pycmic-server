from pycmicserver.csv_parser import Csv_parser

"""Tests que comprueban la ruta force_update pertenecientes a la historia
de usuario administrador"""

#Nuevo usuario desde CSV
def test_force_update_new(client,monkeypatch):
    def new_user(file):
        return [{'usercode':123654, 'name':'TEST3', 'copias_max':1000, 'copias_used': 500}]
    
    monkeypatch.setattr(Csv_parser, 'return_users', new_user)

    r = client.get('/force_update?a=adminkey')
    assert b'"nuevos": 1' in r.data
    assert b'"actualizados": 0' in r.data


#Actualizar la información de un usuario desde el CSV
def test_force_update_update(client,monkeypatch):
    def new_user(file):
        return [{'usercode':12345678, 'name':'TEST3', 'copias_max':1000, 'copias_used': 500}]
    
    monkeypatch.setattr(Csv_parser, 'return_users', new_user)

    r = client.get('/force_update?a=adminkey')
    assert b'"actualizados": 1' in r.data
    assert b'"nuevos": 0' in r.data


#No se recibe ningún usuario, por lo que no se hace nada.
def test_force_update_none(client,monkeypatch):
    def new_user(file):
        return []
    
    monkeypatch.setattr(Csv_parser, 'return_users', new_user)

    r = client.get('/force_update?a=adminkey')
    assert b'"actualizados": 0' in r.data
    assert b'"nuevos": 0' in r.data
