"""Tests que comprueban la ruta get_user pertenecientes a la historia
de usuario cliente"""


"""Pedimos un usuario que existe y nos devuelve su información."""
def test_get_valid_user(client):
    r = client.get('/get_user/12345678?a=webkey')
    print(r.data)
    assert b'TEST_USER' in r.data

"""Pedimos un usuario con una clave de autenticación no válida"""
def test_get_user_no_auth(client):
    assert client.get('/get_user/12384').status_code == 403

"""Pedimos un usuario que no existe"""
def test_get_no_valid_user(client):
    assert client.get('/get_user/123?a=webkey').status_code == 404