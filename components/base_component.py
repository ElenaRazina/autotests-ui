from playwright.sync_api import Page, expect
from typing import Pattern
import allure
from tools.logger import get_logger

logger=get_logger("BASE_COMPONENT")
# Pattern  - это тип стандартной библиотеки python, означает регулярное выражение

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        step=f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

        # для аргумента expected_url ожидается регулярное выражение
        # to_have_url - проверяет, что текущий URL соответствует ожидаемому URL