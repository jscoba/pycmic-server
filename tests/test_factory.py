from pycmicserver import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_status(client):
    r = client.get('/status')
    assert b'ok' in r.data

def test_info(client):
    r = client.get('/info')
    assert b'jscoba' in r.data
    assert b'pycmic-server' in r.data
    assert b'Apache' in r.data