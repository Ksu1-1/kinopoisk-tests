"""API-тесты для Кинопоиска."""

import json
import allure


def test_search_movie_by_name(api_client):
    """Тест поиска фильма по названию."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    query = config["search_query"]

    # Вызываем метод из нашего API-хелпера
    response = api_client.search_movie(query)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    data = response.json()

    with allure.step(f"Проверить, что в результатах есть '{query}'"):
        assert len(data["docs"]) > 0
        assert query.lower() in data["docs"][0]["name"].lower()
