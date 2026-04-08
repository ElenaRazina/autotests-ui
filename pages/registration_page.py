from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent

#сначала указываем конструктор такой же, как в BasePage,
# чтобы инициализировать супер-класс корректно
# Супер-класс нужен, чтобы вызвать родительский класс
class RegistrationPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        #self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        #self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        #self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        #self.registration_button = page.get_by_test_id('registration-page-registration-button')
        #self.login_link = page.get_by_test_id('registration-page-login-link')
        self.registration_button = Button(page,'registration-page-registration-button', 'Registration button')
        self.login_link = Link(page,'registration-page-login-link', 'Login link')

    def fill_registration_form(self, email:str, username:str, password:str):
        self.registration_form.fill(email, password, username)

    def check_visible_registration_form(self, email:str, username:str, password:str):
        self.registration_form.check_visible(email, password, username)

    def click_registration_button(self):
        self.registration_button.click()
