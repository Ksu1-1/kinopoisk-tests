"""TC-UI-5: Фильтрация по жанру и стране."""

import json
import allure
from playwright.sync_api import Page, expect


def test_filter_by_genre_and_country(page: Page):
    """Фильтрация фильмов по жанру (Комедии) и стране (Россия)."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    base_url = config["ui_base_url"]

    with allure.step("Открыть страницу жанра 'Комедии'"):
        page.goto(f"{base_url}/lists/movies/genre--comedy/", timeout=30000)
        page.locator("h1:has-text('Комедии')").first.wait_for(
            state="visible", timeout=15000
        )

    with allure.step("Применить фильтр 'Российские'"):
        russian_filter = page.locator("text=Российские").first
        russian_filter.click()
        page.locator("h1:has-text('Комедии')").first.wait_for(
            state="visible", timeout=10000
        )

    with allure.step("Проверить, что URL обновился и содержит параметр фильтра"):
        assert "b=russian" in page.url

    with allure.step("Проверить, что фильмы успешно отфильтрованы и отобразились"):
        page.locator("text=Рейтинг Кинопоиска").first.wait_for(
            state="visible", timeout=10000
        )
