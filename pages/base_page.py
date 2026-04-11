from playwright.sync_api import Page
from playwright.sync_api import expect
from typing import Pattern

#этот класс просто реализует методы, которые применимы ко всем остальным страницам
# wait_until="networkidle" - ждать, пока не загрузятся все сетевые запросы"""
class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def reload(self):
        self.page.reload(wait_until="networkidle")

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)