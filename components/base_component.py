from playwright.sync_api import Page, expect
from typing import Pattern
# Pattern  - это тип стандартной библиотеки python, означает регулярное выражение

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)

        # для аргумента expected_url ожидается регулярное выражение
        # to_have_url - проверяет, что текущий URL соответствует ожидаемому URL