"""Page Object страницы результатов поиска."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class SearchResultsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Локаторы результатов поиска
        self.first_result = page.locator(".search-results__item").first.locator("a")
        self.search_results = page.locator(".search-results__item")

    @allure.step("Кликнуть по первому результату поиска")
    def click_first_result(self) -> None:
        self.click_element(self.first_result)

    @allure.step("Проверить, что результаты поиска содержат текст: {text}")
    def verify_results_contain(self, text: str) -> bool:
        return self.search_results.first.locator(f"text={text}").is_visible()
