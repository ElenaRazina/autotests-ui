from components.base_component import BaseComponent
from playwright.sync_api import Page,expect
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text
import allure


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu=CourseViewMenuComponent(page)

        #self.title = page.get_by_test_id('course-widget-title-text')
        #self.image = page.get_by_test_id('course-preview-image')
        #self.max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        #self.min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        #self.estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.title = Text(page, 'course-widget-title-text', 'Course title')
        self.image = Image(page, 'course-preview-image', 'Course image')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')

    @allure.step('Check visible course view at index "{index}"')
    def check_visible(
            self,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
            index: int):
        #expect(self.image.nth(index)).to_be_visible()
        #expect(self.title.nth(index)).to_be_visible()
        #expect(self.title.nth(index)).to_have_text(title)
        #expect(self.max_score_text.nth(index)).to_be_visible()
        #expect(self.max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')
        #expect(self.min_score_text.nth(index)).to_be_visible()
        #expect(self.min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')
        #expect(self.estimated_time_text.nth(index)).to_be_visible()
        #expect(self.estimated_time_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')
        self.image.check_visible(nth=index)
        self.title.check_visible(nth=index)
        self.max_score_text.check_visible(nth=index)
        self.min_score_text.check_visible(nth=index)
        self.estimated_time_text.check_visible(nth=index)
        self.title.check_have_text(title)
        self.max_score_text.check_have_text(f'Max score: {max_score}')
        self.min_score_text.check_have_text(f'Min score: {min_score}')
        self.estimated_time_text.check_have_text(f'Estimated time: {estimated_time}')

