"""TC-UI-1: Успешный поиск фильма по названию."""

import json
import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage


def test_search_movie_by_name(page: Page):
    """Поиск фильма по названию."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    query = config["search_query"]

    with allure.step("Открыть главную страницу"):
        main_page = MainPage(page)
        main_page.open()
        page.locator("input[placeholder*='Фильмы']").wait_for(
            state="visible", timeout=10000
        )

    with allure.step(f"Выполнить поиск: {query}"):
        search_input = page.locator("input[placeholder*='Фильмы']")
        search_input.fill(query)
        search_input.press("Enter")
        page.locator(f"text={query}").first.wait_for(state="visible", timeout=15000)

    with allure.step("Проверить, что открылась страница результатов"):
        assert "/new-search/" in page.url
        expect(page.locator("h2:has-text('Фильмы и сериалы')")).to_be_visible(
            timeout=10000
        )

    with allure.step(f"Проверить наличие '{query}' в результатах"):
        expect(page.locator(f"text={query}").first).to_be_visible()
