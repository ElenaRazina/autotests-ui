from components.base_component import BaseComponent
from playwright.sync_api import expect, Page

from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page, index: int):
        super().__init__(page)

        self.delete_button = Button(page,f"create-course-exercise-{index}-box-toolbar-delete-exercise-button", 'Delete exercise')
        self.subtitle = Text(page,f"create-course-exercise-{index}-box-toolbar-subtitle-text", 'Exercise subtitle')
        self.title_input = Input(page,f"create-course-exercise-form-title-{index}-input", 'Exercise title')
        self.description_input = Input(page,f"create-course-exercise-form-description-{index}-input", 'Exercise description')

    def click_delete_button(self, index: int):
        #delete_button = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-delete-exercise-button")
        self.delete_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str):
        #subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        #title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        #description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(f"#{index + 1} Exercise", index=index)
        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(title, index=index)
        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(description, index=index)

        #expect(subtitle).to_be_visible()
        #expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        #expect(title_input).to_be_visible()
        #expect(title_input).to_have_value(title)

        #expect(description_input).to_be_visible()
        #expect(description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        #title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        #description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        #title_input.fill(title)
        #expect(title_input).to_have_value(title)

        #description_input.fill(description)
        #expect(description_input).to_have_value(description)

        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description, index=index)


