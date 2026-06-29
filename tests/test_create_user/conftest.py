import pytest
from app_driver.http_client.http_client import HttpClient
from tests.config2 import BASE_URL
import uuid

@pytest.fixture(scope="session")
def client():
    """Фикстура HTTP-клиента, существующая на всю тестовую сессию"""
    http_client = HttpClient(base_url = BASE_URL)
    yield http_client
    http_client.close()

@pytest.fixture
def valid_user_data():
    """Валидные данные пользователя со всеми обязательными полями"""
    return {
        "email": f"test_{uuid.uuid4().hex[:8]}@example.com",
        "password": "12345",
        "lastName": "Ivanov",
        "firstName": "Ivan",
        "middleName": "Ivanovich"
    }