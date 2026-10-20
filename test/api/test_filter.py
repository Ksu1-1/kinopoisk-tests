"""TC-3: Успешная фильтрация по жанру и стране."""

import json
import allure


def test_filter_by_genre_and_country(api_client):
    """Фильтрация фильмов по жанру и стране."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    genre = config["genre"]
    country = config["country"]

    with allure.step("Отправить запрос с фильтрами"):
        path = f"{api_client.base_url}/movie"
        params = {"genres.name": genre, "countries.name": country, "limit": 5}
        response = api_client.session.get(path, params=params)

    with allure.step("Проверить статус-код 200"):
        assert (
            response.status_code == 200
        ), f"Ожидался 200, получен {response.status_code}"

    data = response.json()

    with allure.step("Проверить, что количество фильмов не превышает лимит"):
        assert (
            len(data["docs"]) <= 5
        ), f"Ожидалось не более 5, получено {len(data['docs'])}"

    with allure.step(
        f"Проверить жанр '{genre}' и страну '{country}' для каждого фильма"
    ):
        for movie in data["docs"]:
            genres = [g["name"] for g in movie.get("genres", [])]
            countries = [c["name"] for c in movie.get("countries", [])]
            assert (
                genre in genres
            ), f"Фильм '{movie.get('name')}' не имеет жанра '{genre}'"
            assert (
                country in countries
            ), f"Фильм '{movie.get('name')}' не имеет страны '{country}'"
