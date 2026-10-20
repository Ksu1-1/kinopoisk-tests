"""Хелпер для работы с API Кинопоиска."""

import requests
import json
import allure


class KinopoiskAPI:
    def __init__(self) -> None:
        with open("test_data.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.base_url = f"{self.config['api_base_url']}/{self.config['api_version']}"
        self.headers = {"X-API-KEY": self.config["api_key"]}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    @allure.step("Выполнить поиск фильма по запросу: {query}")
    def search_movie(self, query: str) -> dict:
        path = f"{self.base_url}/movie/search"
        params = {"query": query}
        resp = self.session.get(path, params=params)
        return resp

    @allure.step("Получить фильм по ID: {movie_id}")
    def get_movie_by_id(self, movie_id: int) -> dict:
        path = f"{self.base_url}/movie/{movie_id}"
        resp = self.session.get(path)
        return resp
