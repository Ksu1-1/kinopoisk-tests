"""TC-2: Успешное получение фильма по ID."""

import json
import allure


def test_get_movie_by_id(api_client):
    """Получение фильма по ID."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    movie_id = config["movie_id"]
    search_query = config["search_query"]

    response = api_client.get_movie_by_id(movie_id)

    with allure.step("Проверить статус-код 200"):
        assert (
            response.status_code == 200
        ), f"Ожидался 200, получен {response.status_code}"

    data = response.json()

    with allure.step("Проверить, что ID фильма совпадает"):
        assert data["id"] == movie_id, f"Ожидался ID {movie_id}, получен {data['id']}"

    with allure.step(f"Проверить, что название содержит '{search_query}'"):
        assert (
            search_query.lower() in data["name"].lower()
        ), f"Ожидалось '{search_query}', получено '{data['name']}'"

    with allure.step("Проверить наличие обязательных полей"):
        assert "year" in data, "Отсутствует поле year"
        assert "type" in data, "Отсутствует поле type"
