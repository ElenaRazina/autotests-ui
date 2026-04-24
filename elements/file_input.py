from elements.base_element import BaseElement
import allure
from tools.logger import get_logger

logger=get_logger("FILE_INPUT")

class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return 'file input'

    def set_input_files(self, file: str, nth:int=0,**kwargs):
        step=f'Set file "{file}" to the {self.type_of} "{self.name}"'
        # Для input элементов не нужно добавлять .locator('input'), так как элемент уже является input
        # locator = self.page.get_by_test_id(self.locator.format(**kwargs))
        with allure.step(step):
            formatted_locator = self.locator.format(**kwargs)
            locator = self.page.get_by_test_id(formatted_locator).nth(nth)
            logger.info(step)
            locator.set_input_files(file)