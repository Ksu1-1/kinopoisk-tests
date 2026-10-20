"""TC-UI-2: Успешный поиск персоны по имени."""

import json
import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage


def test_search_person_by_name(page: Page):
    """Поиск персоны по имени."""
    with open("test_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    person_name = config["person_name"]

    with allure.step("Открыть главную страницу"):
        main_page = MainPage(page)
        main_page.open()
        page.locator("input[placeholder*='Фильмы']").wait_for(
            state="visible", timeout=10000
        )

    with allure.step(f"Выполнить поиск персоны: {person_name}"):
        search_input = page.locator("input[placeholder*='Фильмы']")
        search_input.fill(person_name)
        search_input.press("Enter")
        page.locator(f"text={person_name}").first.wait_for(
            state="visible", timeout=15000
        )

    with allure.step("Проверить, что открылась страница результатов"):
        assert "/new-search/" in page.url
        expect(page.locator("h2:has-text('Персоны')")).to_be_visible(timeout=10000)

    with allure.step(f"Проверить наличие '{person_name}' в результатах"):
        expect(page.locator(f"text={person_name}").first).to_be_visible()
