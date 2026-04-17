from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from typing import Pattern
from elements.text import Text
from elements.icon import Icon
from elements.button import Button
import allure


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Формируем локаторы динамически
        #self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        #self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        #self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        #expect(self.icon).to_be_visible()
        #expect(self.title).to_be_visible()
        #expect(self.title).to_have_text(title)
        #expect(self.button).to_be_visible()
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.button.check_visible()


    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
