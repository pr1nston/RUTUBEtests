import requests
import json
import pytest
from requests.exceptions import HTTPError


def test_get_request():
    # URL для тестирования
    url = "https://rutube.ru/api/marketplace/products/?client=wdp"

    # Отправка GET запроса
    response = requests.get(url)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка формата ответа

