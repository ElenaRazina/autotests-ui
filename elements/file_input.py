from elements.base_element import BaseElement

class FileInput(BaseElement):
    def set_input_files(self, file: str, nth:int=0,**kwargs):
        # Для input элементов не нужно добавлять .locator('input'), так как элемент уже является input
        # locator = self.page.get_by_test_id(self.locator.format(**kwargs))
        formatted_locator = self.locator.format(**kwargs)
        locator = self.page.get_by_test_id(formatted_locator).nth(nth)
        locator.set_input_files(file)