"""TC-4: Запрос без авторизации (негативный)."""

import json
import allure
import requests


def test_search_without_auth():
    """Запрос к API без заголовка авторизации."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    base_url = f"{config['api_base_url']}/{config['api_version']}"
    query = config["search_query"]

    with allure.step("Отправить запрос БЕЗ заголовка X-API-KEY"):
        path = f"{base_url}/movie/search"
        params = {"query": query}
        response = requests.get(path, params=params)

    with allure.step("Проверить статус-код 401 или 403"):
        assert response.status_code in [
            401,
            403,
        ], f"Ожидался 401 или 403, получен {response.status_code}"

    with allure.step("Проверить наличие сообщения об ошибке"):
        data = response.json()
        assert "message" in data or "error" in data, "Отсутствует сообщение об ошибке"
