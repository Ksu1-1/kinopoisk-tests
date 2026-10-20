"""Базовый класс для всех страниц."""

from playwright.sync_api import Page, expect
import allure


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Открыть URL: {url}")
    def open_url(self, url: str) -> None:
        self.page.goto(url)

    @allure.step("Ввести текст '{text}' в элемент")
    def fill_input(self, locator, text: str) -> None:
        locator.fill(text)

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator) -> None:
        locator.click()

    @allure.step("Ожидать видимости элемента")
    def wait_for_visible(self, locator, timeout: int = 10000) -> None:
        expect(locator).to_be_visible(timeout=timeout)
