from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        #self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        #self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        #self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.email_input = Input(page, 'registration-form-email-input',  'Email input')
        self.username_input = Input(page, 'registration-form-username-input', 'Username input')
        self.password_input = Input(page, 'registration-form-password-input', 'Password input')

    @allure.step('Fill registration form')
    def fill(self, email: str, password: str, username: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step('Check visible registration form')
    def check_visible(self, email: str, password: str, username: str):
        #expect(self.email_input).to_have_value(email)
        #expect(self.username_input).to_have_value(username)
        #expect(self.password_input).to_have_value(password)
        self.email_input.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()
        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)
