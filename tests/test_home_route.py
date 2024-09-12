from hello import app
from flask import request



def test_home_route():
    response =  app.test_client().get('/')
    assert response.status_code == 200
    assert b'Hello Salano' in response.data


# test hello parameter route
def test_hello_route():
    with app.test_client() as c:
        response = c.get('/hello/Tanis')
        #assert requests.args['name'] == 'Tanis'
        assert response.status_code == 200
        assert b'Hello Tanis' in response.data
        assert response.data.decode('utf-8') == 'Hello Tanis'


test_home_route()
test_hello_route()