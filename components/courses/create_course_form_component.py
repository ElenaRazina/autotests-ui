from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        #self.title= page.get_by_test_id('create-course-form-title-input').locator('input')
        #self.estimated_time= page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        #self.description= (
            # При поиске поля описания будет найдено два тега textarea, берем первый из них
            #page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        #)
        #self.max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        #self.min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')
        self.title = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_time = Input(page, 'create-course-form-estimated-time-input', 'Estimated time')
        self.description = Textarea(page, 'create-course-form-description-input', 'Description')
        self.max_score = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.min_score = Input(page, 'create-course-form-min-score-input', 'Min score')

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str):
        #expect(self.title).to_be_visible()
        #expect(self.title).to_have_value(title)

        #expect(self.estimated_time).to_be_visible()
        #expect(self.estimated_time).to_have_value(estimated_time)

        #expect(self.description).to_be_visible()
        #expect(self.description).to_have_value(description)

        #expect(self.max_score).to_be_visible()
        #expect(self.max_score).to_have_value(max_score)

        #expect(self.min_score).to_be_visible()
        #expect(self.min_score).to_have_value(min_score)
        self.title.check_visible()
        self.estimated_time.check_visible()
        self.description.check_visible()
        self.max_score.check_visible()
        self.min_score.check_visible()
        self.title.check_value(title)
        self.estimated_time.check_value(estimated_time)
        self.description.check_value(description)
        self.max_score.check_value(max_score)
        self.min_score.check_value(min_score)

    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str):
        self.title.fill(title)
        self.estimated_time.fill(estimated_time)
        self.description.fill(description)
        self.max_score.fill(max_score)
        self.min_score.fill(min_score)

