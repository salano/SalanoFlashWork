from methods import app

# test login route
def test_form_post_route():
    data = {
        'nm': 'Tanis'
    }
    with app.test_client() as c:
        response = c.post('/login', data=data)
        # redirect
        assert response.status_code == 302 
        assert b'/welcome/Tanis' in response.data


test_form_post_route()