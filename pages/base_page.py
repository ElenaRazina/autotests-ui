from playwright.sync_api import Page
from playwright.sync_api import expect
from typing import Pattern
import allure
from tools.logger import get_logger

logger=get_logger("BASE_PAGE")

#этот класс просто реализует методы, которые применимы ко всем остальным страницам
# wait_until="networkidle" - ждать, пока не загрузятся все сетевые запросы"""
class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        step=f'Opening the url "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")

    def reload(self):
        step=f'Reloading page with url "{self.page.url}"'
        with allure.step(step):
            #{self.page.url} подставит текущую страницу, на которую перезагружаем
            logger.info(step)
            self.page.reload(wait_until="networkidle")

    def check_current_url(self, expected_url: Pattern[str]):
        step=f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)