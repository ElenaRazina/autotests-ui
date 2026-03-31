from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

class EmptyCoursesListPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.navbar=NavbarComponent(page)
        self.sidebar=SidebarComponent(page)
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        self.empty_view_create_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_view_icon(self):
        expect(self.empty_view_icon).to_be_visible()

    def check_visible_view_title(self):
        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

    def check_visible_view_description(self):
        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    def check_visible_view_create_button(self):
        expect(self.empty_view_create_button).to_be_visible()


