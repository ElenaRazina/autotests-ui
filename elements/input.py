from playwright.sync_api import expect, Locator
from elements.base_element import BaseElement

class Input(BaseElement):
    # Переопределяем метод get_locator
    # через super() вызываем метод get_locator() из родительского класса BaseElement
    def get_locator(self, nth: int=0, **kwargs) ->Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value:str, nth:int=0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value:str, nth:int=0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)

    #def set_input_files(self, file: str, nth:int=0, **kwargs):
        # Для input элементов не нужно добавлять .locator('input'), так как элемент уже является input
        #locator = self.page.get_by_test_id(self.locator.format(**kwargs))
    #    formatted_locator = self.locator.format(**kwargs)
    #    locator = self.page.get_by_test_id(formatted_locator).nth(nth)
    #    locator.set_input_files(file)