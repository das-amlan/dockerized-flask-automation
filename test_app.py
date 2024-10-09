from app import app

def test_home():
    """Tests the response of the home route ("/") of the Flask application."""
    # Simulate a GET request to the home route
    response = app.test_client().get("/") 

    # Assert successful response
    assert response.status_code == 200, "Expected a 200 status code (success)"  
    # Assert expected response data
    assert response.data == b"Hello World! How is it going??"  
