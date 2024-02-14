import pytest
from src.handler import predict_text

@pytest
def test_handler():
    text = predict_text()
    assert text == "4"