"""Page Object главной страницы Кинопоиска."""

from playwright.sync_api import Page
from pages.base_page import BasePage
import json
import allure


class MainPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        with open("test_data.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.ui_base_url = self.config["ui_base_url"]

        # Локаторы главной страницы
        self.search_input = page.get_by_placeholder("Фильмы, сериалы, персоны")
        self.search_button = page.locator("button[type='submit']").first

    @allure.step("Открыть главную страницу Кинопоиска")
    def open(self) -> None:
        self.page.goto(self.ui_base_url, timeout=30000)

    @allure.step("Выполнить поиск по запросу: {query}")
    def search(self, query: str) -> None:
        self.fill_input(self.search_input, query)
        self.click_element(self.search_button)
