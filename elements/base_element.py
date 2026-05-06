from playwright.sync_api import Page, Locator, expect
import allure
from tools.logger import get_logger
from elements.ui_covrage import tracker
from ui_coverage_tool import ActionType, SelectorType

logger=get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator:str, name:str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self)->str:
        return 'base element'


    def get_locator(self, nth: int=0, **kwargs)->Locator:
    # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        step=f'Getting locator with "data-testid"={locator}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
    # .format() подставляет значение в строку
    # kwargs - это словарь ("id":123, "type": "card") именованных аргументов, ** распаковывает словарь в id=123, "type"=card
    # Однако на реальных проектах вы можете столкнуться с ситуацией, когда не все элементы имеют атрибуты data-testid?
    # или их нет вовсе. В таких случаях вместо метода get_by_test_id, вам нужно будет
    # использовать метод self.page.locator(locator), передавая в аргумент locator полные значения XPath или CSS селекторов.
    # locator = self.locator.format(**kwargs) означает взять шаблон self.locator, подставить в него значения из kwargs,
    # сохранить результат в переменную locator.
        # Возвращаем объект локатора
            return self.page.get_by_test_id(locator).nth(nth)
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

    def get_raw_locator(self, nth:int=0, **kwargs)->str:
        return f"//*[@data-testid='{self.locator.format(**kwargs)}'][{nth+1}]"
    #найти любой элемент (*), у которого есть атрибут data-testid такой-то с таким-то индексом

    def track_coverage(self,action_type:ActionType, nth:int=0,**kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH)


    def click(self, nth: int=0, **kwargs):
        step=f'Clicking {self.type_of} "{self.name}"'
        with allure.step(step):
            locator=self.get_locator(nth, **kwargs)
            logger.info(step) # логгер размещаем сразу перед действием
            locator.click()
        #tracker.track_coverage(selecor=self.get_raw_locator(nth,**kwargs),
        #                       action_type=ActionType.CLICK,
        #                       selector_type=SelectorType.XPATH)

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int=0, **kwargs):
        step=f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            locator=self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        #tracker.track_coverage(
        #    selecor=self.get_raw_locator(
        #        nth,
        #        **kwargs),
        #    action_type=ActionType.VISIBLE,
        #    selector_type=SelectorType.XPATH)

        self.track_coverage(
            ActionType.VISIBLE,
            nth, **kwargs)

    def check_have_text(self, text:str, nth: int=0, **kwargs):
        step=f'Checking that {self.type_of} "{self.name}" has text "{text}"'
        with allure.step(step):
            locator=self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        #tracker.track_coverage(
        #    selecor=self.get_raw_locator(
        #        nth,
        #        **kwargs),
        #    action_type=ActionType.TEXT,
        #    selector_type=SelectorType.XPATH)

        self.track_coverage(
            ActionType.TEXT,
            nth, **kwargs)

