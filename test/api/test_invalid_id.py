"""TC-5: Запрос с невалидным ID (негативный)."""

import json
import allure


def test_get_movie_with_invalid_id(api_client):
    """Запрос с невалидным ID фильма."""
    invalid_id = "invalid_id_string"

    with allure.step(f"Отправить запрос с невалидным ID: {invalid_id}"):
        path = f"{api_client.base_url}/movie/{invalid_id}"
        response = api_client.session.get(path)

    with allure.step("Проверить статус-код 400 или 404"):
        assert response.status_code in [
            400,
            404,
        ], f"Ожидался 400 или 404, получен {response.status_code}"

    with allure.step("Проверить наличие сообщения об ошибке"):
        data = response.json()
        assert "message" in data or "error" in data, "Отсутствует сообщение об ошибке"
