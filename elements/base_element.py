from playwright.sync_api import Page, Locator, expect

class BaseElement:
    def __init__(self, page: Page, locator:str, name:str):
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs)->Locator:
    # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
    # .format() подставляет значение в строку
    # kwargs - это словарь ("id":123, "type": "card") именованных аргументов, ** распаковывает словарь в id=123, "type"=card
    # Однако на реальных проектах вы можете столкнуться с ситуацией, когда не все элементы имеют атрибуты data-testid?
    # или их нет вовсе. В таких случаях вместо метода get_by_test_id, вам нужно будет
    # использовать метод self.page.locator(locator), передавая в аргумент locator полные значения XPath или CSS селекторов.
    # locator = self.locator.format(**kwargs) означает взять шаблон self.locator, подставить в него значения из kwargs,
    # сохранить результат в переменную locator.
        # Возвращаем объект локатора
        return self.page.get_by_test_id(locator)
 # эта строка берет уже готовую строку locator и передает ее в self.page.get_by_test_id(...)
 # get_by_test_id - метод для поиска элемента по атрибуту data-testid
 # Пример: element = BaseElement(page, "page-{index}-title", "Page Title")
# locator = element.get_locator(index=1)  # подставляется index=1 в локатор
# или self.locator="product-{id}-{type}"
# get_locator(id=123,type='card')
# kwargs={"id:=123,"type"='card'}
# locator='product-123-card'
# page.get_by_test_id('product-123-card'), т.е. метод вернет Locator элемента с таким data-testid
# Так делается, чтобы не писать много почти одинаковых локаторов вручную.
# Функция def get_locator(self, **kwargs) позволяет динамически сформировать локатор

    def click(self,**kwargs):
        locator=self.get_locator(**kwargs)
        locator.click()

    def check_visible(self,**kwargs):
        locator=self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text:str, **kwargs):
        locator=self.get_locator(**kwargs)
        expect(locator).to_have_text(text)

