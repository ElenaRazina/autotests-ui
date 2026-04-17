from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
import allure

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        #self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        #self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.email_input = Input(page, 'login-form-email-input', 'Email input')
        self.password_input = Input(page, 'login-form-password-input', 'Password input')

    @allure.step('Fill login form')
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step('Check visible login form')
    def check_visible(self, email: str, password: str):
        #expect(self.email_input).to_have_value(email)
        #expect(self.password_input).to_have_value(password)
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)




