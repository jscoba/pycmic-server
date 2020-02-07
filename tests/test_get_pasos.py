"""Tests que comprueban la ruta get_pasos pertenecientes a la historia
de usuario cliente
El usuario al conectarse a través del cliente web pide su número de copias
restantes utilizando su dni como usuario. Para esto previamente se ha tenido
que asociar el número de dni al código de usuario, ya que estos no tienen
por qué coincidir.

"""


"""Pedimos un usuario que existe y nos devuelve su información."""
def test_get_valid_user_dni(client):
    r = client.get('/get_pasos/12345678A?a=webkey')
    print(r.data)
    assert b'TEST_USER' in r.data

"""Pedimos un usuario con una clave de autenticación no válida"""
def test_get_dni_no_auth(client):
    assert client.get('/get_pasos/12384').status_code == 403

"""Pedimos un usuario que no existe"""
def test_get_no_valid_user_dni(client):
    assert client.get('/get_pasos/123?a=webkey').status_code == 404