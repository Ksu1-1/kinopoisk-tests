"""TC-UI-3: Успешное открытие карточки фильма."""

import json
import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage


def test_open_movie_card(page: Page):
    """Открытие карточки фильма из результатов поиска."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    query = config["search_query"]

    with allure.step("Открыть главную страницу и выполнить поиск"):
        main_page = MainPage(page)
        main_page.open()
        page.locator("input[placeholder*='Фильмы']").wait_for(
            state="visible", timeout=10000
        )

        search_input = page.locator("input[placeholder*='Фильмы']")
        search_input.fill(query)
        search_input.press("Enter")
        page.locator(f"text={query}").first.wait_for(state="visible", timeout=15000)

    with allure.step("Кликнуть по первому результату поиска"):
        first_result = page.locator("a[href*='/film/']").first
        first_result.click()
        page.locator("h1").first.wait_for(state="visible", timeout=15000)

    with allure.step("Проверить, что открылась страница фильма"):
        assert "/film/" in page.url

    with allure.step("Проверить наличие названия фильма (заголовка h1)"):
        expect(page.locator("h1").first).to_be_visible()
