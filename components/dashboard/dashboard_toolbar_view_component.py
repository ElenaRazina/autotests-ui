from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
import allure

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        #self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.dashboard_title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard title')

    @allure.step('Check visible dashboard title')
    def check_visible(self):
        #expect(self.dashboard_title).to_be_visible()
        #expect(self.dashboard_title).to_have_text('Dashboard')
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')
