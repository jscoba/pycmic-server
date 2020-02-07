"""Tests que comprueban la ruta link_user pertenecientes a la historia
de usuario cliente

Para conocer el número de impresiones restantes de un usuario desde la página web del
centro este debe ligar su código de usuario de la impresora a su usuario de la web, que
suele ser el DNI. Esta ruta hace la conexión entre ambos datos y permite en futuras
peticiones conocer los pasos restantes a través del DNI.

"""

def test_link_user(client):
    r = client.get('/link_user/987654321/12345678B?a=webkey')
    assert b'OK' in r.data
    r = client.get('/get_pasos/12345678B?a=webkey')
    assert b'987654321' in r.data

def test_link_user_not_valid(client):
    r = client.get('/link_user/11111111/12345678B?a=webkey')
    assert r.status_code == 404
   