from playwright.sync_api import expect, Locator
from elements.base_element import BaseElement
import allure
from tools.logger import get_logger

logger=get_logger("INPUT")

class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return 'input'
    # Переопределяем метод get_locator
    # через super() вызываем метод get_locator() из родительского класса BaseElement
    def get_locator(self, **kwargs) ->Locator:
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value:str, **kwargs):
        step=f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value:str, **kwargs):
        step=f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

    def set_input_files(self, file: str, **kwargs):
        step=f'Set file "{file}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
        # Для input элементов не нужно добавлять .locator('input'), так как элемент уже является input
            locator = self.page.get_by_test_id(self.locator.format(**kwargs))
            logger.info(step)
            locator.set_input_files(file)
