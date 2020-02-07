"""Tests que comprueban la ruta get_users pertenecientes a la historia
de usuario administrador

Esta función permite al administrador guardar una copia de seguridad de los
usuarios así como conocer estadísticas de impresión de todos los usuarios
a la vez.
"""


"""Pedimos la lista de todos los usuarios."""
def test_get_valid_user(client):
    r = client.get('/get_users?a=adminkey')
    print(r.data)
    assert b'TEST_USER' in r.data
    assert b'TEST2' in r.data

"""Pedimos un usuario con una clave de autenticación no válida"""
def test_get_user_no_auth(client):
    assert client.get('/get_users?a=webkey').status_code == 403