"""TC-UI-4: Сортировка фильмов по рейтингу."""

import json
import allure
from playwright.sync_api import Page, expect


def test_sort_movies_by_rating(page: Page):
    """Сортировка фильмов по рейтингу."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    base_url = config["ui_base_url"]

    with allure.step("Открыть страницу жанра 'Комедии'"):
        page.goto(f"{base_url}/lists/movies/genre--comedy/", timeout=30000)
        page.locator("h1:has-text('Комедии')").first.wait_for(
            state="visible", timeout=15000
        )

    with allure.step("Найти выпадающий список сортировки 'По порядку' и кликнуть"):
        sort_button = page.locator("text=По порядку").first
        sort_button.click()

    with allure.step("Выбрать сортировку 'По рейтингу'"):
        rating_option = page.locator("text=По рейтингу").first
        rating_option.click()
        page.locator("h1:has-text('Комедии')").first.wait_for(
            state="visible", timeout=10000
        )

    with allure.step("Проверить, что URL обновился и содержит параметр сортировки"):
        assert "sort=rating" in page.url

    with allure.step("Проверить, что фильмы успешно отобразились"):
        page.locator("text=Рейтинг Кинопоиска").first.wait_for(
            state="visible", timeout=10000
        )
