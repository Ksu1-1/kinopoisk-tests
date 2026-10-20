"""Фикстуры для тестов."""

import pytest
from playwright.sync_api import Browser, Page
from api.kinopoisk_api import KinopoiskAPI
import allure


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API-тестов."""
    with allure.step("Инициализация API клиента"):
        return KinopoiskAPI()


@pytest.fixture(scope="session")
def browser_context(browser: Browser):
    """Фикстура для создания контекста браузера."""
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    yield context
    context.close()


@pytest.fixture
def page(browser_context):
    """Фикстура для создания новой страницы."""
    page = browser_context.new_page()
    yield page
    page.close()
