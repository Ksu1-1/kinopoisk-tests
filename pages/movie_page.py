"""Page Object страницы фильма."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class MoviePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Локаторы страницы фильма
        self.movie_title = page.locator("h1").first
        self.movie_year = page.locator("text=1972").first
        self.movie_rating = page.locator("[class*='rating']").first

    @allure.step("Получить название фильма")
    def get_movie_title(self) -> str:
        return self.movie_title.inner_text()

    @allure.step("Проверить, что год фильма виден")
    def is_year_visible(self) -> bool:
        return self.movie_year.is_visible()
