from playwright.sync_api import Page
#этот класс просто реализует методы, которые применимы ко всем остальным страницам
# wait_until="networkidle" - ждать, пока не загрузятся все сетевые запросы"""
class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def reload(self):
        self.page.reload(wait_until="networkidle")