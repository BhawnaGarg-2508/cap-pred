# test_app.py

import pytest
from flask import Flask
from app import app, predict_dummy, calculate_result_display

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_dummy():
    input_data = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    result = predict_dummy(input_data)
    assert result == 42.0

def test_calculate_result_display():
    result = 42.0
    display_result = calculate_result_display(result)
    assert display_result == "42.000"

# Add more tests as needed

if __name__ == '__main__':
    pytest.main()
